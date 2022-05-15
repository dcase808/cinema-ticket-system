import pymongo
from secret import CONNECTION_STRING


client = pymongo.MongoClient(CONNECTION_STRING)
db = client.cinema
movies = db.movies
shows = db.shows
users = db.users