from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ingredients")
def ingredients():
    pantry = ['Salt', 'Pepper', 'Cheese: Mild Cheddar', 'Chicken Breast', 'Beans: Black', 'Cabbage']
    title = "Virutal Pantry"
    return render_template("ingredient_list.html", title = title, pantry = pantry)
     
if __name__ == "__main__":
    app.run()
