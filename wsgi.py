from flask import Flask, jsonify

app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Le Wagon'},
    }

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def products():
    result = jsonify(list(PRODUCTS.values()))
    return result

@app.route('/api/v1/product/<int:id>')
def getProduct(id):
    if id not in PRODUCTS.keys():
        return jsonify({"message": "Product not found"}), 404
    return jsonify(PRODUCTS[id])