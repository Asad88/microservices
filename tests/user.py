import unittest
import requests
from flask import request, session, redirect, url_for, Flask ,json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import ServiceUnavailable
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../services/cmovies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


def save():
    data = {'db': 'database.db', 'tn': 'users'}
    try:
        r = requests.post("http://127.0.0.1:5000/getall", data=data)
    except requests.exceptions.ConnectionError:
        raise ServiceUnavailable("The Movie service is unavailable.")
    return r.text


def login():
        data = {'db': 'database.db', 'tn': 'users', 'pr': 'admin'}
        try:
            r = requests.post("http://127.0.0.1:5000/getall", data=data)
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailable("The Movie service is unavailable.")
        return r.text


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5000/"

    def test_login(self):
        valid_user = 'admin'
        data = login()
        actual_reply = str(False)
        data2 = str(True)
        if valid_user not in data:
                data2 = str(False)
        for movieid, expected in GOOD_RESPONSES.items():
            if movieid == valid_user:
                actual_reply = str(True)
        self.assertEquals(actual_reply,data2)

   # def test_wrong_user_login(self):
    #    """ Test /users/<username> for non-existent user"""
     #   invalid_user = ['jim_the_duck_guy','hhh']
      #  p = " names = '" + invalid_user[0] + "' and pass = '" + invalid_user[1] + "'"
       # data = {'db': 'database.db', 'tn': 'users', 'pr': p}
        #actual_reply = requests.post("{}".format(self.url), data)

        #self.assertFalse(actual_reply, "Got {} user record but expected {}".format(
         #   actual_reply, False
        #))


GOOD_RESPONSES = {
  "admin" : {
    "id": "chris_rivers",
    "name": "admin",
    "last_active":1360031010
  },
  "peter_curley" : {
    "id": "peter_curley",
    "name": "Peter Curley",
    "last_active": 1360031222
  }
}

if __name__ == "__main__":
    unittest.main()
