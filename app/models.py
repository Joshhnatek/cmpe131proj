from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # pantry = db.relationship('Pantry', backref='owner')

    def __repr(self):
        return '{}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

"""
class Pantry(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    # connect to a growable list of ingredients
    """