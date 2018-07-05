import unittest
import requests


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5000/"

    def test_login(self):
        valid_user = ['admin', '1']
        p = " names = '" + valid_user[0] + "' and pass = '" + valid_user[1] + "'"
        data = {'db': 'database.db', 'tn': 'users', 'pr': p}
        actual_reply = requests.post("{}".format(self.url), data)

        self.assertTrue(actual_reply, "Got {} user record but expected {}".format(
                             actual_reply, True
                             ))

    def test_wrong_user_login(self):
        """ Test /users/<username> for non-existent user"""
        invalid_user = ['jim_the_duck_guy','hhh']
        p = " names = '" + invalid_user[0] + "' and pass = '" + invalid_user[1] + "'"
        data = {'db': 'database.db', 'tn': 'users', 'pr': p}
        actual_reply = requests.post("{}".format(self.url), data)

        self.assertFalse(actual_reply, "Got {} user record but expected {}".format(
            actual_reply, False
        ))


GOOD_RESPONSES = {
  "chris_rivers" : {
    "id": "chris_rivers",
    "name": "Chris Rivers",
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
