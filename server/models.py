from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy


db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    reviews = db.relationship('Review', back_populates='customer', cascade='all, delete-orphan')
    items = association_proxy('reviews', 'item')

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    reviews = db.relationship('Review', back_populates='item', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Item {self.id}, {self.name}, {self.price}>'


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String, nullable=False)  # <-- This is the key fix!
    rating = db.Column(db.Integer, nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    customer = db.relationship('Customer', back_populates='reviews')
    item = db.relationship('Item', back_populates='reviews')
