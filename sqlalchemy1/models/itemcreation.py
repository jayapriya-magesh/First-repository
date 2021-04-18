
from db import db


class itemmodel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('storemodel')

    def __init__(self, name, price,store_id):

        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_username(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

"""


from db import db

class itemmodel(db.Model):
    __tablename__ = 'items'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(70))
    price = db.Column(db.Float(precision=2))

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def json(self):
        return {"name": self.name,"price": self.price}

    @classmethod
    def find_by_username(cls,name):
        return cls.query.filter_by(name=name).first()

    def safe_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
"""   #dont know it is throwing error
