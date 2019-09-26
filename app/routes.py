from app import app
from flask import render_template

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ingredients")
def ingredients():
    pantry = []
    title = "Virutal Pantry"
    return render_template("ingredient_list.html", title = title, pantry = pantry)
     
if __name__ == "__main__":
    app.run()
