from app import db
from model.entities import Application

class Credentials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    application_id = db.relationship('Application', backref='Credentials', lazy=True)