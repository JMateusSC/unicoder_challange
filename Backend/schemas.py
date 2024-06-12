from pydantic import BaseModel
import datetime
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class Requestdetails(BaseModel):
    email:str
    password:str
        

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class Changepassword(BaseModel):
    email:str
    old_password:str
    new_password:str


class TokenCreate(BaseModel):
    user_id:str
    access_token:str
    refresh_token:str
    status:bool
    created_date:datetime.datetime
    

class ProductCreate(BaseModel):
    name:str
    description:str
    price:int


class ProductUpdate(BaseModel):
    id: int
    name:str
    description:str
    price:int


class ProductFetch(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None


class ProductDelete(BaseModel):
    id: int