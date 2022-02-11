from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    name: str
    username: str
    email: str
    password: str
    location: str
    birth_date: datetime
    age: int
    job: str
    description: Optional[str] = None
    interests: Optional[List[str]] = None
    phone_number: str
    first_name: Optional[str]
    last_name: Optional[str]
    sex: str
    is_verified: Optional[bool] = None
    has_subscription: Optional[bool] = None
    photo_album: Optional[List[str]] = None
    profile_picture: Optional[str] = None
    disliked_user_list: Optional[List[str]] = None
    liked_user_list: Optional[List[str]] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {

            "user": {
                "name": "string",
                "username": "string",
                "email": "string",
                "password": "string",
                "location": "string",
                "birth_date": "2022-02-09T09:15:18.857000",
                "age": 0,
                "job": "string",
                "description": "string",
                "interests": [
                    "string"
                ],
                "phone_number": "string",
                "first_name": "string",
                "last_name": "string",
                "sex": "string",
                "is_verified": "true",
                "has_subscription": "true",
                "photo_album": [
                    "string"
                ],
                "profile_picture": "string",
                "disliked_user_list": [
                    "string"
                ],
                "liked_user_list": [
                    "string"
                ]
            }
        }


class UpdateUser(BaseModel):
    name: str
    username: str
    password: str
    location: str
    birth_date: datetime
    age: int
    job: str
    description: Optional[str] = None
    interests: List[str]
    phone_number: str
    first_name: str
    last_name: str
    sex: str
    is_verified: bool
    has_subscription: bool
    photo_album: List[str]
    profile_picture: str
    disliked_user_list: List[str]
    liked_user_list: List[str]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "user": {
                "name": "string",
                "username": "string",
                "password": "string",
                "location": "string",
                "birth_date": "2022-02-09T09:15:18.857000",
                "age": 0,
                "job": "string",
                "description": "string",
                "interests": [
                    "string"
                ],
                "phone_number": "string",
                "first_name": "string",
                "last_name": "string",
                "sex": "string",
                "is_verified": "true",
                "has_subscription": "true",
                "photo_album": [
                    "string"
                ],
                "profile_picture": "string",
                "disliked_user_list": [
                    "string"
                ],
                "liked_user_list": [
                    "string"
                ]
            }
        }
