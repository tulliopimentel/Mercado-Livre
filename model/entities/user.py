from app import db
from model.entities import Credentials

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    credentials = db.relationship('Credentials', backref='User', lazy=True)

    def is_valid_credentials(self, email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            return True
        else:
            return False