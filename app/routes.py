from app import app
from flask import render_template
from app import forms

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ingredients")
def ingredients():
    pantry = []
    title = "Virutal Pantry"
    return render_template("ingredient_list.html", title = title, pantry = pantry)
     
@app.route("/login")
def login():
    form = User_Form()
    return render_template("login.html")

if __name__ == "__main__":
    app.run()
