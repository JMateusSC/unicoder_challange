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
    dead_line:datetime.datetime
    end_date:datetime.datetime
    expected_time:int
    registered_time:int

class TaskFetch(BaseModel):
    id: int
    status:Optional[str] = None
    title:Optional[str] = None
    description:Optional[str] = None
    dead_line:Optional[datetime.datetime] = None
    end_date:Optional[datetime.datetime] = None
    expected_time:Optional[int] = None
    registered_time:Optional[int] = None

class TaskDelete(BaseModel):
    id: int
