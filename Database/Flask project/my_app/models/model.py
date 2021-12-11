from flask import Blueprint, render_template
from my_app import db

bp = Blueprint('model', __name__)



class Item(db.Model):
    __table_args__ = ({"schema" : "shopping"})
    __table__ = db.Model.metadata.tables['item']
    

    def __repr__(self):
        return str(self.index)


class Sales(db.Model):
    __table__ = db.Model.metadata.tables['sales']

    def __repr__(self):
        return str(self.index)


class Rating(db.Model):
    __table__ = db.Model.metadata.tables['rating']

    def __repr__(self):
        return str(self.index)


class Users(db.Model):
    __table__ = db.Model.metadata.tables['user']

    def __repr__(self):
        return str(self.id)


# class Ingr(db.Model):
#     __table__ = db.Model.metadata.tables['ingredients_csv']

#     def __repr__(self):
#         return str(self.id)