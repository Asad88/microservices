import sqlite3
import unittest

import flask
import requests
import json
import sys

from flask import Flask

from services import movies
from services.movies import movie_list

from werkzeug.exceptions import ServiceUnavailable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../microservices/services/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def movie_list():
        data = {'db': 'database.db' , 'tn': 'movies'}
        try:
            r = requests.post("http://127.0.0.1:5000/getall",data=data)
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailable("The Movie service is unavailable.")
        return r.text


def sqlite_insert(conn, table, row):
    cols = ', '.join('"{}"'.format(col) for col in row.keys())
    vals = ', '.join(':{}'.format(col) for col in row.keys())
    sql = 'INSERT INTO "{0}" ({1}) VALUES ({2})'.format(table, cols, vals)
    conn.cursor().execute(sql, row)
    conn.commit()


class TestMoviesService(unittest.TestCase):

    def setUp(self):
        self.url = "http://127.0.0.1:5001/movielist"

    def test_order_movie(self):
        movieid = movie_list()
        movieid2 ="503ab8df-5d5a-4e7d-a4fc-bcb39d2e6ab9"
        if movieid2 not in movieid:
            data = {}
        else:
            data = movieid2
        actual_reply = {}
        for movieid, expected in GOOD_RESPONSES.items():
            if movieid == movieid2:
                actual_reply = movieid2

        self.assertEqual(data, actual_reply)

    def test_add_movie(self):
        record = str({'title':'TEST MOVIE', 'director':'Tomer Admon', 'rating':'9.3'})
        data = {'db': 'database.db', 'tn': 'movies', 'record': record}
        try:
            r = requests.post("http://127.0.0.1:5000/add_record", data=data)
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailable("The Movie service is unavailable.")
        print(r.text)
        self.assertIn('TEST MOVIEss', str(json.loads(r.text)))


GOOD_RESPONSES = {
  "720d006c-3a57-4b6a-b18f-9b713b073f3c": {
    "title": "The Good Dinosaur",
    "rating": 7.4,
    "director": "Peter Sohn",
    "id": "720d006c-3a57-4b6a-b18f-9b713b073f3c"
  },
  "a8034f44-aee4-44cf-b32c-74cf452aaaae": {
    "title": "The Martian",
    "rating": 8.2,
    "director": "Ridley Scott",
    "id": "a8034f44-aee4-44cf-b32c-74cf452aaaae"
  },
  "503ab8df-5d5a-4e7d-a4fc-bcb39d2e6ab9": {
    "title": "The Night Before",
    "rating": 7.4,
    "director": "Jonathan Levine",
    "id": "96798c08-d19b-4986-a05d-7da856efb697"
  },
  "267eedb8-0f5d-42d5-8f43-72426b9fb3e6": {
    "title": "Creed",
    "rating": 8.8,
    "director": "Ryan Coogler",
    "id": "267eedb8-0f5d-42d5-8f43-72426b9fb3e6"
  }
}
if __name__ == "__main__":
    unittest.main()
