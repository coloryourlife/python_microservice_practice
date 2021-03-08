import unittest
import json
import sys
sys.path.append('../Chapter02')
from flask_basic import app as _app

class TestApp(unittest.TestCase):
    def test_help(self):
        # To connect with app, we should make a instance of FlaskClient
        app = _app.test_client()

        # Call /api endpoint
        hello = app.get('/api')

        # Check the response
        body = json.loads(str(hello.data, 'utf8'))
        self.assertEqual(body['Hello'], 'World!')

if __name__ == '__main__':
    unittest.main()
