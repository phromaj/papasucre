from fastapi import FastAPI
from pydantic import BaseModel, Field
import pymongo
from bson import ObjectId
from typing import Optional
from models import user
app = FastAPI()
client = pymongo.MongoClient(
    "mongodb+srv://rob:rob123456@cluster0.hv6ea.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test


@app.get('/users')
async def list_users():
    users = []
    for item in db.users.find():
        users.append(user.UserModel(**item))
    return {'users': users}


@app.post('/users')
async def create_user(user: user.UserModel):
    if hasattr(user, 'id'):
        delattr(user, 'id')
    ret = db.users.insert_one(user.dict(by_alias=True))
    user.id = ret.inserted_id
    return {'user': user}
