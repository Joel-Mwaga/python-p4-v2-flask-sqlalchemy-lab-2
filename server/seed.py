#!/usr/bin/env python3

from server.app import app
from server.models import db, Customer, Item, Review

with app.app_context():
    db.drop_all()
    db.create_all()

    c1 = Customer(name='Alice')
    c2 = Customer(name='Bob')
    i1 = Item(name='Mug', price=9.99)
    i2 = Item(name='T-Shirt', price=19.99)
    db.session.add_all([c1, c2, i1, i2])
    db.session.commit()

    r1 = Review(comment='Great mug!', rating=5, customer=c1, item=i1)
    r2 = Review(comment='Nice shirt.', rating=4, customer=c2, item=i2)
    db.session.add_all([r1, r2])
    db.session.commit()
    print("Seeded database!")
