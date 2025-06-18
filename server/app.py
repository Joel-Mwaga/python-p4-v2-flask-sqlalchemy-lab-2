from flask import Flask, jsonify, request
from flask_migrate import Migrate

from models import db, Customer, Item, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'


@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([
        {
            'id': c.id,
            'name': c.name,
            'items': [i.id for i in c.items]
        } for c in customers
    ])


@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([
        {
            'id': i.id,
            'name': i.name,
            'price': i.price
        } for i in items
    ])


@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([
        {
            'id': r.id,
            'comment': r.comment,
            'rating': r.rating,
            'customer_id': r.customer_id,
            'item_id': r.item_id
        } for r in reviews
    ])


# Optional: Add POST routes for seeding/testing
@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    c = Customer(name=data['name'])
    db.session.add(c)
    db.session.commit()
    return jsonify({'id': c.id, 'name': c.name}), 201


@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    i = Item(name=data['name'], price=data['price'])
    db.session.add(i)
    db.session.commit()
    return jsonify({'id': i.id, 'name': i.name, 'price': i.price}), 201


@app.route('/reviews', methods=['POST'])
def create_review():
    data = request.json
    r = Review(comment=data['comment'], rating=data.get('rating'), customer_id=data['customer_id'], item_id=data['item_id'])
    db.session.add(r)
    db.session.commit()
    return jsonify({'id': r.id, 'comment': r.comment}), 201


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)
