from fastapi import Depends, FastAPI, Query, status, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from db_connect import movies, shows, users
from models import Movie, SeatIn, SeatsOut, Show, ShowOut, Token
from bson import ObjectId
from fastapi.security import OAuth2PasswordRequestForm
from auth import authenticate_user, create_token, validate_token

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_headers=['*'],
    allow_methods=['*']
)

@app.get('/validate', tags=['auth'])
async def validate(username: str = Depends(validate_token)):
    return username

@app.post('/token', response_model=Token, tags=['auth'])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = create_token({'sub': form_data.username})
    return {'access_token': token, 'token_type': 'bearer'}
    

@app.post('/movies', tags=['movies'])
async def add_movie(movie: Movie, username: str = Depends(validate_token)):
    if movies.count_documents({'_id': movie.title}) > 0:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    entry = {
        '_id': movie.title,
        'title': movie.title,
        'poster': movie.poster,
        'desc': movie.desc
    }
    movies.insert_one(entry)
    return entry

@app.get('/movies/{title}', response_model=Movie, tags=['movies'])
async def get_movie(title: str):
    find_movies = movies.find({'_id': title})
    return find_movies[0]

@app.get('/movies', response_model=list[Movie], tags=['movies'])
async def get_all_movies():
    output = []
    find_movies = movies.find()
    for movie in find_movies:
        output.append(movie)
    return output

@app.get('/shows', response_model=list[ShowOut], tags=['shows'])
async def get_shows(title: str):
    movies = []
    find_shows = shows.find({'title': title})
    for show in find_shows:
        show['id'] = str(show['_id'])
        movies.append(show)
    return movies

@app.get('/shows-all', response_model=list[ShowOut], tags=['shows'])
async def get_all_shows():
    movies = []
    find_shows = shows.find({})
    for show in find_shows:
        show['id'] = str(show['_id'])
        movies.append(show)
    return movies

@app.get('/seats/{id}', response_model=SeatsOut)
async def get_seats(id: str):
    id = ObjectId(id)
    find_shows = shows.find({'_id': id})
    count = shows.count_documents({'_id': id})
    print(count)
    if count > 0:
        out = {
            'seats_taken': find_shows[0]['seats_taken']
        }
        return out
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.post('/shows', response_model=Show, tags=['shows'])
async def add_show(show: Show, username: str = Depends(validate_token)):
    entry = {
        'title': show.title,
        'date': show.date,
        'seats_taken': show.seats_taken,
    }
    shows.insert_one(entry)
    return entry

@app.delete('/shows/{id}', response_model=ShowOut, tags=['shows'])
async def remove_show(id: str, username: str = Depends(validate_token)):
    id = ObjectId(id)
    show = shows.find_one_and_delete({'_id': id})
    if show:
        out = {
            'id': str(show['_id']),
            'title': show['title'],
            'date': show['date'],
            'seats_taken': show['seats_taken']
        }
        return out
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.delete('/movies/{id}', tags=['movies'])
async def remove_movie(id: str, username: str = Depends(validate_token)):
    movie = movies.find_one_and_delete({'_id': id})
    if movie:
        out = {
            'id': str(movie['_id']),
            'title': movie['title'],
            'poster': movie['poster'],
            'desc': movie['desc']
        }
        return out
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.patch('/shows/{id}', tags=['shows'])
async def add_taken_seats(id: str, seats: SeatIn):
    id = ObjectId(id)
    count = shows.count_documents({'_id': id})
    if count > 0:
        shows.update_one({'_id': id}, {'$push': {'seats_taken': {'$each': seats.seats}}})
        return True
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)