from app import db, login_manager
from flask_login import UserMixin
from model.entities import Credentials

class User(UserMixin, db.Model):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        self.is_active = True

    def get_id(self):
        return str(self.id)
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    credentials = db.relationship('Credentials', backref='User', lazy=True)
    is_active = db.Column(db.Boolean(), default=True)

    def is_valid_credentials(self, email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            return True
        else:
            return False
        
    @login_manager.user_loader
    def load_user(email):
        return User.query.filter_by(email=email).first()
