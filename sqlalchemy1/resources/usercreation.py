from flask import Flask
from flask_restful import Resource,reqparse
from flask_jwt import JWT,jwt_required

from models.usercreation import usermodel


class userregistration(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This is a mandatory field"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This is a mandatory field"
    )
    def post(self):
        data=userregistration.parser.parse_args()
        if usermodel.usernamemapping(data['username']):
            return {"message": "The user already exists"}
        user = usermodel(data['username'],data['password'])
        print(data['username'])
        print(data['password'])
        user.save_to_db()
        return {"message": "The user created successfully"},201


