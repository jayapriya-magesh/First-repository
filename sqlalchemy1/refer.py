import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

class items(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='This is a mandatory field'
    )
    @jwt_required()
    def get(self,name):
        item = items.find_by_username(name)
        if item:
            return item
        else:
            return {"message":"The item doesnt exists"}

    @classmethod
    def find_by_username(cls,name):
        connection = sqlite3.connect('sql.db')
        cursor = connection.cursor()
        query = "select * from items where name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {"items":{"name": row[0],"price":row[1]}},200

    def post(self,name):
        data=items.parser.parse_args()
        connection=sqlite3.connect('sql.db')
        cursor=connection.cursor()
        query='select * from items where name=?'
        result=cursor.execute(query,(name,))
        row=result.fetchone()
        if row:
            connection.close()
            return {"message": "The item already exists"},400
        else:
            item={'name': name,'price': data['price']}
            quert = "Insert into items values(?,?)"
            cursor.execute(quert, (item['name'], item['price'],))
            connection.commit()
            connection.close()
            return item,201

    def put(self,name):
        data = items.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        connection = sqlite3.connect('sql.db')
        cursor = connection.cursor()
        query = 'select * from items where name=?'
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        if row:
            quert='update items set price = ? where name =?'
            cursor.execute(quert,(item['price'], item['name']))

        else:
            quert = "Insert into items values(?,?)"
            cursor.execute(quert, (item['name'], item['price'],))

        connection.commit()
        connection.close()
        return item, 200

    def delete(self,name):
        connection=sqlite3.connect('sql.db')
        cursor=connection.cursor()
        query='delete from items where name=?'
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()
        return {"message": 'The item is successfully deleted'},200

class itemslist(Resource):
    def get(self):
        connection=sqlite3.connect('sql.db')
        cursor=connection.cursor()
        query='select * from items'
        result=cursor.execute(query)
        items=[]
        for x in result:
            items.append(x)   # or items.append({"name": x[0],"price":x[1]})
        connection.close()
        return {'items': items}






