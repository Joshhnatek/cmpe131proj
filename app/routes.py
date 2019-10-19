from app import app
from flask import render_template, redirect, url_for
from app.forms import User_Form

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/ingredients")
def ingredients():
    pantry = []
    title = "Virutal Pantry"
    return render_template("ingredient_list.html", title = title, pantry = pantry)
     
@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = User_Form()
    title = "Login"
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template("login.html", form = form, title = title)

if __name__ == "__main__":
    app.run()
