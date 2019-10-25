from app import app
from app.models import User
from flask import render_template, flash, redirect, request
from app.forms import User_Form, RegistrationForm
from flask_login import current_user, login_user

@app.route("/")
def home():
    
    return render_template("home.html")

@app.route("/ingredients")
def ingredients():
    pantry = []
    title = "Virutal Pantry"
    
    return render_template("ingredient_list.html", title = title, pantry = pantry)
     
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("ingredients"))

    form = User_Form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user is None or not user.check_password(form.password.data):
            flash("Invalid email or password")
            return redirect(url_for("login"))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("ingredients"))


    title = "Login"
    return render_template("login.html", form = form, title = title)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('ingredients'))
    
    form = RegistrationForm()

    
    if form.validate_on_submit():
        user = User(username=form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration complete!")
        return redirect(url_for('login'))

    return render_template('register.html', title = 'Register', form = form)
if __name__ == "__main__":
    app.run(debug=True)
