from flask import Flask, jsonify, Request, abort
import itertools

app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Le Wagon'},
    }

START_INDEX = len(PRODUCTS) + 1
IDENTIFIER_GENERATOR = itertools.count(START_INDEX)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def products():
    result = jsonify(list(PRODUCTS.values()))
    return result

@app.route('/api/v1/products/<int:id>')
def get_product(id):
    if id not in PRODUCTS.keys():
        abort(404)
    return jsonify(PRODUCTS[id])

@app.route('/api/v1/products/<int:id>', methods=["DELETE"])
def delete_one_product(id):
    product = PRODUCTS.pop(id, None)

    if product is None:
        abort(404)
    return '', 204