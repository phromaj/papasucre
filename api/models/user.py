from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class UserModel(BaseModel):
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
    disliked_user_list: List[str]
    liked_user_list: List[str]
