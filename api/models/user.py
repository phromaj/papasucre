from bson import ObjectId
from typing import Optional
from pydantic import BaseModel, Field
from models import pyObjectId


class UserModel(BaseModel):
    id: Optional[pyObjectId.PyObjectId] = Field(alias='_id')
    name: str
    username: str
    email: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
