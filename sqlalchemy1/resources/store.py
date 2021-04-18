from flask_restful import Resource
from models.store import storemodel

class store(Resource):
    def get(self,name):
        s= storemodel.find_by_name(name)
        if s:
            return s.json(),200
        else:
            return {"message": "The item doesnt exists"},404

    def post(self,name):
        if storemodel.find_by_name(name):
            return {"message": "The store name already exists"}
        s=storemodel(name)
        try:
            s.save_to_db()
        except:
            return {'message':'An uexpected error has occured'},500

        return s.json(),201

    def delete(self,name):
        s=storemodel.find_by_name(name)
        if s:
            s.delete_from_db()
            return {'message':'successfully deleted'}
        else:
            return {'message':'store doesnt exists'}

class storelist(Resource):
    def get(self):
        return {'items': [x.json() for x in storemodel.query.all()]}
