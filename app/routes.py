from app import app, db
from flask import render_template, redirect, url_for, flash, request
from app.forms import User_Form, Registration_Form, Add_Ingredient_Form
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/ingredients")
@login_required
def ingredients():
    pantry = [] #temp object
    title = "Virtual Pantry"
    return render_template("ingredient_list.html", title = title, pantry = pantry)

@app.route("/stock_pantry")

def stock_pantry():
    title = "Stock Pantry"
    form = Add_Ingredient_Form()
    pantry = []
    return render_template("stock_pantry.html", title = title, form = form, 
                    pantry = pantry)
     
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = User_Form()
    title = "Login"
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
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
        flash("You are now a registered user!")
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()
