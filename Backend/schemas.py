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
    

class TaskCreate(BaseModel):
    status:str
    title:str
    description:str
    dead_line:datetime.datetime
    creation_date:datetime.datetime
    end_date:datetime.datetime
    expected_time:int
    registered_time:int

class TaskUpdate(BaseModel):
    id: int
    status:str
    title:str
    description:str
    dead_line:str
    end_date:str
    expected_time:str
    registered_time:str

class TaskFetch(BaseModel):
    id: int
    status:Optional[str]
    title:Optional[str]
    description:Optional[str]
    dead_line:Optional[str]
    creation_date:Optional[str]
    end_date:Optional[str]
    expected_time:Optional[str]
    registered_time:Optional[str]

class TaskDelete(BaseModel):
    id: int
