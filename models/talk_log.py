from .base import db

class TalkLog(db.Model):
    __tablename__ = 'talk_log'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Text)
    talk = db.Column(db.Text)