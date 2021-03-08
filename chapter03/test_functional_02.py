import unittest
import json
import sys
sys.path.append('../Chapter02')

_404 = "The requested URL was not found on the server. " \
    " If you entered the URL manually please check your" \
    "spelling and try again."

class TestApp(unittest.TestCase):
    def setUp(self):
        from flask_error import app as _app
        # To connect with app make a instance of FlaskClient
        self.app = _app.test_client()

    def test_raise(self):
        # When we call /api flask_error will make an error then return 500 error in json format
        hello = self.app.get('/api')
        if(sys.version_info > (3, 0)):
            body = json.loads(str(hello.data, 'utf8'))
        else:
            body = json.loads(str(hello.data).encode("utf8"))
        self.assertEqual(body['code'], 500)

    def test_proper_404(self):
        # Call endpoint which does not exist on purpose
        hello = self.app.get('/asdfjhadkjf')

        # The status code should be 404 since the endpoint doesn't exist
        self.assertEqual(hello.status_code, 404)

        # Also, the description of the error should be return in Json format.

        if(sys.version_info > (3,0)):
            body = json.loads(str(hello.data, 'utf8'))
        else:
            body = json.loads(str(hello.data).encode("utf8"))
        self.assertEqual(body['code'], 404)
        self.assertEqual(body['message'], '404 Not Found')
        self.assertEqual(body['description'], _404)

if __name__ == '__main__':
    unittest.main()
