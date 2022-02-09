from typing import List

from fastapi import FastAPI, HTTPException
import pymongo
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

from models import userModel


app = FastAPI()
client = pymongo.MongoClient(
    "mongodb+srv://rob:rob123456@cluster0.hv6ea.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test


@app.get('/users', response_description="List all users", response_model=List[userModel.User])
def list_users():
    students = []
    for student in db.users.find():
        students.append(student)
    return students


@app.get("/users/{email}", response_description="Get a single user", response_model=userModel.User)
def show_user(email: str):
    if (user := db.users.find_one({"email": email})) is not None:
        return user
    raise HTTPException(status_code=404, detail=f"User with {email} not found")


@app.post('/users', response_description="Add new user", response_model=userModel.User)
def create_user(user: userModel.User):
    db["users"].insert_one(user.dict(by_alias=True))
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(user))


@app.put('/users/{email}', response_description="Update a user", response_model=userModel.UpdateUser)
def update_user(email: str, user: userModel.UpdateUser):
    user = {k: v for k, v in user.dict().items() if v is not None}

    if len(user) >= 1:
        update_result = db["users"].update_one({"email": email}, {"$set": user})
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
