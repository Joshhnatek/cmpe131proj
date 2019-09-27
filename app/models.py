
class User(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    pantry = db.relationship('Pantry', backref='owner')

    def __repr(self):
        return '{}'.format(self.username)

class Pantry(db.Model):
    user_id = db.Column(db.Integer, db.ForeighnKey('owner.id'))