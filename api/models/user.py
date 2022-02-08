from bson import ObjectId
from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime
from models import pyObjectId


class UserModel(BaseModel):
    id: Optional[pyObjectId.PyObjectId] = Field(alias='_id')
    name: str
    username: str
    email: str
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
    disliked_userlist: List[str]
    liked_userlist: List [str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
