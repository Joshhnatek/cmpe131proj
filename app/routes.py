from flask import current_app as app
from . import db, login
from flask import render_template, redirect, url_for, flash, request, jsonify
from .forms import User_Form, Registration_Form, Add_Ingredient_Form, Remove_Ingredient_Form
from flask_login import current_user, login_user, logout_user, login_required
from .models import User, Ingredients, Pantry, recipes, recipeIng
from werkzeug.urls import url_parse


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/ingredients")
@login_required
def ingredients():
    # items = Pantry.query.filter_by(user_id=current_user.id).all()
    items = Pantry.get_users_items(current_user.id)
    pantry = []
    
    for ingredient in items:
        i = Ingredients.get_ingredient_name(ingredient.ingredient_id) 
        pantry.append(i)
    title = "Virtual Pantry"
    return render_template("ingredient_list.html", title = title, pantry = pantry)

@app.route("/recipes_search")
@login_required
def recipes_search(): 
    items = Pantry.query.filter_by(user_id=current_user.id).all()
    available_recipes = []
    for ingredient in items:
        recipe_ingredients = recipeIng.query.filter_by(ingredient_id = ingredient.ingredient_id).all()
        for r in recipe_ingredients:
            recipe = recipes.query.filter_by(id = r.recipe_id).first()
            available_recipes.append(recipe.recipeN)

    return render_template("recipe_list.html", title = "recipes", recipes = available_recipes)



@app.route("/stock_pantry", methods = ['GET', 'POST'])
def stock_pantry():
    title = "Stock Pantry"

    form = Add_Ingredient_Form()

    items = Ingredients.query.with_entities(Ingredients.category).distinct()
    form.category.choices = [(i.category, i.category) for i in items ]

    form.name.choices = [(i.id, i.name) for i in Ingredients.query.filter_by(category=items[0].category).all()]

    if request.method == "POST": 
        ingredient = Ingredients.query.filter_by(category=form.category.data).filter_by(id=form.name.data).first()
    
        if(Pantry.query.filter_by(user_id= current_user.id, ingredient_id= ingredient.id).first()):
            flash("Selected Ingredient is already in your pantry", "stock_error")
            return(redirect(url_for('stock_pantry')))
        else:
            item = Pantry(user_id = current_user.id, ingredient_id = ingredient.id, ingredient_name=ingredient.name)
            db.session.add(item)
            db.session.commit()
            flash("Added Selected Ingredients!", "stock_success")
            return redirect(url_for('ingredients'))
        
    return render_template("stock_pantry.html", title = title, form = form)
     
@app.route('/get_items/<category>')
def get_items(category):
    collection = Ingredients.query.filter_by(category=category).all()
    
    itemsArray = []
    for i in collection:
        itemObj = {}
        itemObj['id'] = i.id
        itemObj['name'] = i.name
        itemsArray.append(itemObj)

    return jsonify({'items' : itemsArray})

@app.route('/remove_ingredient', methods=['GET', 'POST'])
def remove_ingredient():
    title = 'Remove Ingredient'

    form = Remove_Ingredient_Form()

    items = Pantry.query.filter_by(user_id=current_user.id).all()

    form.pantry.choices = [(i.ingredient_id, i.ingredient_name) for i in items]

    if request.method == 'POST':
        target = Ingredients.query.get(form.pantry.data)
        ingredient = Pantry.query.filter_by(user_id=current_user.id, ingredient_id=target.id).first()

        db.session.delete(ingredient)
        db.session.commit()
        flash("Removed selected ingredient", "remove_success")
        return redirect(url_for('ingredients'))
    return render_template("remove.html", title=title, form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = User_Form()
    title = "Login"
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password", "login_error")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template("login.html", form = form, title = title)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Registration_Form()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You are now a registered user!", "register_success")
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()