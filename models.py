from exts import db
from datetime import datetime


class ManagerModel(db.Model):
    __tablename__ = "manager"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(1000), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, )
    sex = db.Column(db.String(2), nullable=False)
    tel = db.Column(db.String(20), nullable=False, unique=True)
    live = db.Column(db.String(3), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)


