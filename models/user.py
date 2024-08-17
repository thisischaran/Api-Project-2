

from db import db


class dbusertable(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.String(30), unique=True,nullable=False, )
    password = db.Column(db.String(200), nullable= False)


class dblogouttable(db.Model):
    __tablename__ = "logout"

    id = db.Column(db.Integer, primary_key = True)
    tokens =db.Column(db.String(200), nullable = False)