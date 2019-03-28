import base64
import hashlib
from app import app, hello_world, USERS
from math_func import add, subtract, multiply, divide
from student import Student
import unittest


class MathTestCAse(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 7), 10)

    def test_subtract(self):
        self.assertEqual(subtract(3, 7), -4)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(divide(3, 7), 3 / 7)


class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.student1 = Student('Pavel', 'Nikulin', 1234)
        self.student2 = Student('Maxim', 'Averin', 36000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.student1.email, 'p.nikulin@innopolis.ru')
        self.assertEqual(self.student2.email, 'm.averin@innopolis.ru')

        self.student1.first = 'Dmitry'
        self.student2.last = 'Smirnov'

        self.assertEqual(self.student1.email, 'd.nikulin@innopolis.ru')
        self.assertEqual(self.student2.email, 'm.smirnov@innopolis.ru')

    def test_full_name(self):
        self.assertEqual(self.student1.full_name, 'Pavel Nikulin')
        self.assertEqual(self.student2.full_name, 'Maxim Averin')

        self.student1.first = 'Dmitry'
        self.student2.last = 'Smirnov'

        self.assertEqual(self.student1.full_name, 'Dmitry Nikulin')
        self.assertEqual(self.student2.full_name, 'Maxim Smirnov')

    def test_is_in_36k_club(self):
        self.assertFalse(self.student1.is_in_36k_club)
        self.assertTrue(self.student2.is_in_36k_club)

        self.student1.scholarship = 36000
        self.student2.scholarship = 12000

        self.assertTrue(self.student1.is_in_36k_club)
        self.assertFalse(self.student2.is_in_36k_club)


class ServerTestCase(unittest.TestCase):
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

    def test_registration_page(self):
        valid_credentials = base64.b64encode(b'panddromas:Barselona1414').decode('utf-8')
        response = self.app.post('/registration', headers={'Authorization': 'Basic ' + valid_credentials})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(USERS['panddromas'], hashlib.sha256('Barselona1414'.encode()).hexdigest())

        response = self.app.post('/registration')
        self.assertEqual(response.status_code, 400)

        response = self.app.get('/registration')
        self.assertEqual(response.status_code, 405)

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
        response = self.app.get('/secret_stuff', headers={'Authorization': 'Basic ' + valid_credentials})
        self.assertEqual(response.status_code, 200)

        invalid_credentials = base64.b64encode(b'valeriy:val1212').decode('utf-8')
        response = self.app.get('/secret_stuff', headers={'Authorization': 'Basic ' + invalid_credentials})
        self.assertEqual(response.status_code, 401)

        response = self.app.get('/secret_stuff')
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
