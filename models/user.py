

from db import db


class dbusertable(db.model):
    __tablename__ = "users"

    userid = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(200), nullable= False)


class dblogouttable(db.model):
    __tablename__ = "logout"

    tokens =db.Column(db.String(200), nullable = False)