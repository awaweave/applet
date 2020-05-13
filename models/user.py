from .base import db


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text)
    password = db.Column(db.Text)

