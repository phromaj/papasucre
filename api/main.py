from typing import List

import pymongo

from fastapi import FastAPI, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

from models import userModel
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from auth import AuthHandler


class AuthDetails(BaseModel):
    email: str
    password: str


users = []
auth_handler = AuthHandler()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = pymongo.MongoClient(
    "mongodb+srv://rob:rob123456@cluster0.hv6ea.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test


@app.get('/unprotected')
def unprotected():
    return {'hello': 'world'}


@app.get('/protected')
def protected(email=Depends(auth_handler.auth_wrapper)):
    return {'name': email}


@app.get('/users', response_description="List all users", response_model=List[userModel.User])
def list_users():
    users = []
    for user in db.users.find():
        users.append(user)
    return users


@app.get("/users/{email}", response_description="Get a single user", response_model=userModel.User)
def show_user(email: str):
    if (user := db.users.find_one({"email": email})) is not None:
        return user
    raise HTTPException(status_code=404, detail=f"User with {email} not found")


@app.post('/users', response_description="Add new user", response_model=userModel.User)
def create_user(user: userModel.User):
    if (u := db.users.find_one({"email": user.email})) is not None:
        raise HTTPException( status_code=401, detail='email already exists')
    user.password = auth_handler.get_password_hash(user.password)
    db["users"].insert_one(user.dict(by_alias=True))
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(user))


@app.post('/user-login')
def login(auth: AuthDetails ):
    user = None
    for u in db.users.find():
        if u['email'] == auth.email:
            user = u
            break

    if (user is None) or (not auth_handler.verify_password(auth.password, user['password'])):
        raise HTTPException(
            status_code=401, detail='Invalid email and/or password')
    token = auth_handler.encode_token(user['email'])
    return {'token': token}


@app.put('/users/{email}', response_description="Update a user", response_model=userModel.UpdateUser)
def update_user(email: str, user: userModel.UpdateUser):
    user = {k: v for k, v in user.dict().items() if v is not None}

    if len(user) >= 1:
        update_result = db["users"].update_one(
            {"email": email}, {"$set": user})
        if update_result.modified_count == 1:
            if (
                    updated_user := db["users"].find_one({"email": email})
            ) is not None:
                return updated_user

    if (existing_user := db["users"].find_one({"email": email})) is not None:
        return existing_user

    raise HTTPException(status_code=404, detail=f"user {email} not found")


@app.delete("/users/{email}", response_description="Remove a user from db")
def delete_user(email: str):
    if db.users.delete_one({"email": email}) != 0:
        return JSONResponse(status_code=200, content="deleted")

    raise HTTPException(status_code=404, detail=f"user {email} not found")
