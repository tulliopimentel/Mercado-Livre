from model.entities.User import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserService:
    @staticmethod
    def is_valid_credentials(email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            return True
        else:
            return False