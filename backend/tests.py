import base64

from app import app, hello_world
import unittest


class TestCase(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        # Disable sending emails during unit testing
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)

    def test_hello_world(self):
        self.assertEqual(hello_world('some'), 'Hello, World!')
        self.assertEqual(hello_world(), 'Hello, bloody world!')
        self.assertEqual(hello_world('doom'), 'Hello, bloody world!')

    def test_login_page(self):
        valid_credentials = base64.b64encode(b'valeriy:val1212').decode('utf-8')
        response = self.app.get('/login', headers={'Authorization': 'Basic ' + valid_credentials})
        self.assertEqual(response.status_code, 200)

        invalid_credentials = base64.b64encode(b'sdfsdf:324kj').decode('utf-8')
        response = self.app.get('/login', headers={'Authorization': 'Basic ' + invalid_credentials})
        self.assertEqual(response.status_code, 401)

        response = self.app.get('/login')
        self.assertEqual(response.status_code, 400)

    def test_secret_stuff_page(self):
        valid_credentials = base64.b64encode(b'indionapolis:moscow1147').decode('utf-8')
        print(valid_credentials)
        response = self.app.get('/secret_stuff', headers={'Authorization': 'Basic ' + valid_credentials})
        self.assertEqual(response.status_code, 200)

        invalid_credentials = base64.b64encode(b'valeriy:val1212').decode('utf-8')
        response = self.app.get('/secret_stuff', headers={'Authorization': 'Basic ' + invalid_credentials})
        self.assertEqual(response.status_code, 401)

        response = self.app.get('/secret_stuff')
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
