from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_read_many_products(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.
        self.assertEqual(response.status_code, 200)

    def test_read_success_one_product(self):
        response = self.client.get("/api/v1/product/1")
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertEqual(set(product), set({'id': 1, 'name': 'Skello'})) # 2 is not a mistake here.
        self.assertEqual(response.status_code, 200)
        
    def test_read_failed_one_product(self):
        response = self.client.get("/api/v1/product/100")
        message = response.json
        self.assertEqual(set(message),set({"message": "Product not found"})) # 2 is not a mistake here.
        self.assertEqual(response.status_code, 404)