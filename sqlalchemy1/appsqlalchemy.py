from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from db import db

from resources.usercreation import userregistration
from authorization import authenticate,identity
from resources.itemcreation import items,itemslist
from resources.store import store,storelist

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key='JP'
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWT(app,authenticate,identity)

db.init_app(app)

api.add_resource(items,'/item/<string:name>')
api.add_resource(itemslist,'/items')
api.add_resource(store,'/store/<string:name>')
api.add_resource(storelist,'/stores')
api.add_resource(userregistration,'/register')

if __name__ == '__main__':
    app.run(port=5000,debug=True)
