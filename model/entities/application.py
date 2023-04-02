from app import db
from model.entities import Credentials

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(200))
    user_application_id = db.Column(db.String(200))
    client_id = db.Column(db.String(200))
    client_secret = db.Column(db.String(200))
    code = db.Column(db.String(200))
    credentials_id = db.Column(db.Integer, db.ForeignKey('credentials.id'))