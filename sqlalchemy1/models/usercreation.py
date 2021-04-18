import sqlite3
from flask import Flask
from flask_restful import Resource,reqparse
from flask_jwt import JWT,jwt_required
from db import db

class usermodel(db.Model):  # the first letter of Model(M) should always be in caps
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(70))
    password = db.Column(db.String(70))

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def usernamemapping(cls,username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def useridmapping(cls, _id):
        return cls.query.filter_by(id = _id ).first()






