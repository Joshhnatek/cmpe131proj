from app import app
from flask import render_template
from app.forms import User_Form

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
    form = User_Form()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid email or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('ingredients'))


    title = "Login"
    return render_template("login.html", form = form, title = title)

if __name__ == "__main__":
    app.run()
