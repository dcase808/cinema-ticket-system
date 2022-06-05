from datetime import datetime
from pydantic import BaseModel
from fastapi import Body

class Movie(BaseModel):
    _id: str
    title: str
    poster: str
    desc: str


class Show(BaseModel):
    title: str
    date: datetime
    seats_taken: list[int] | None = Body([])

class ShowOut(Show):
    id: str

class SeatsOut(BaseModel):
    seats_taken: list[int]

class User(BaseModel):
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str
    