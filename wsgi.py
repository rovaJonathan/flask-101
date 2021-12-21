from flask import Flask, jsonify, request, abort
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

@app.route(f'/api/v1/products', methods=['POST'])
def create_product():
    payload = request.get_json()

    if payload is None:
        abort(400)

    name = payload.get('name')

    if name is None:
        abort(400)

    if name == '' or not isinstance(name, str):
        abort(422)

    next_id = next(IDENTIFIER_GENERATOR)
    PRODUCTS[next_id] = {'id' : next_id , 'name' : name }
    return jsonify(PRODUCTS[next_id]), 201