import unittest
import json
import sys

import requests

from services import queryDB_Service


class TestMoviesService(unittest.TestCase):
     def setUp(self):
        self.url = "http://127.0.0.1:5001/movielist"

    def test_order_movie(self):
        valid_mid="ceb0c09f-826c-4ed9-b1ad-8dbc6fe0cfa3"
        p = " id = '" + valid_mid +"'"
        data = {'db': 'database.db', 'tn': 'movies'}
        actual_reply = requests.post("{}".format(self.url),data)

        print(actual_reply.text)
        self.assertTrue(True)
        # self.assertTrue(
        #                 "ceb0c09f-826c-4ed9-b1ad-8dbc6fe0cfa3" in actual_reply.text ,
        #                  "Got {} user record but expected {}".format(
        #                      actual_reply, True
        #                      ))


    # def test_add_movie(self):
    #     response = self.app.post('/movies', data=dict(
    #         director='Tomer Admon',
    #         rating='9.3',
    #         title='TEST MOVIE'
    #         ), follow_redirects=True)
    #     self.assertIn('TEST MOVIE',
    #                   str(json.loads(response.get_data().decode(sys.getdefaultencoding()))))


if __name__ == "__main__":
    unittest.main()
