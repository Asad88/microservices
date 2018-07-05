import unittest
import requests


class TestShowTimesService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5000/deletebyid"

    def test_delete_records(self):
        """ Test /showtimes/<date> for all known showtimes"""
        mid="ceb0c09f-826c-4ed9-b1ad-8dbc6fe0cfa3"
        actual_reply = requests.post("{}".format(self.url),data=("id = "+mid))


        self.assertTrue(mid not in actual_reply,
                             "Got {} showtimes but expected {}"
                             )


if __name__ == "__main__":
    unittest.main()
