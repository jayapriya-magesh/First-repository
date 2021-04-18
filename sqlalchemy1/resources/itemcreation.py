import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.itemcreation import itemmodel

class items(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='This is a mandatory field'
    )
    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help='Every item should have a storeid'
    )
    @jwt_required()
    def get(self,name):
        item = itemmodel.find_by_username(name)
        if item:
            return item.json()
        else:
            return {"message":"The item doesnt exists"}


    def post(self,name):
        if itemmodel.find_by_username(name):
            return {"message": "The item already exists"},400
        data=items.parser.parse_args()
        item=itemmodel(name,data['price'],data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"message":"An error occured while inserting an item"},500
        return item.json(),201


    def put(self,name):
        data = items.parser.parse_args()
        item=itemmodel.find_by_username(name)
        if item:
            item.price=data['price']
        else:
            item=itemmodel(name,data['price'],data['store_id'])

        item.save_to_db()
        return item.json()


    def delete(self,name):
        item=itemmodel.find_by_username(name)
        if item:
            item.delete_from_db()
            return {"message": "The item is successfully deleted"},200
        else:
            return {"message": "The item doesnt exists"},404


class itemslist(Resource):
    def get(self):
        result = itemmodel.query.all()
        items=[]
        for x in result:
            return {'items': x.json()}   # this will give only the name and price of the item.

# to fetch the id for an item u can use the logic from get call of refer program.

#       return {'items': [item.json() for item in itemmodel.query.all()]},200






