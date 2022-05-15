from datetime import datetime, timedelta
from os import urandom
from hashlib import pbkdf2_hmac

from fastapi import Depends, HTTPException, status
from db_connect import users
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from secret import SECRET_KEY

ouath2_scheme = OAuth2PasswordBearer(tokenUrl='token')

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password):
    salt = urandom(32)
    key = pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        10000
    )
    return key, salt

def verify_password(password, key, salt):
    new_key = pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        10000
    )
    if new_key == key:
        return True
    return False

def authenticate_user(username, password):
    if users.count_documents({'username': username}) > 0:
        user = users.find_one({'username': username})
        if verify_password(password, user['key'], user['salt']):
            return True
    return False

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def validate_token(token: str = Depends(ouath2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = payload.get('sub')
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if users.count_documents({'username': username}) > 0:
        return username
    return False
