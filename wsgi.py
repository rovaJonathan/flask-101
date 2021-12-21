from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/produits')
def products():
    return jsonify({
        1: { 'id': 1, 'name': 'Skello' },
        2: { 'id': 2, 'name': 'Socialive.tv' },
        3: { 'id': 3, 'name': 'best.tv' },
        })