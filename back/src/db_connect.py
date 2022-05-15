import pymongo


CONNECTION_STRING = 'XXX'

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.cinema
movies = db.movies
shows = db.shows
users = db.users