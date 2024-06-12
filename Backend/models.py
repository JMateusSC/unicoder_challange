from sqlalchemy import Column, Integer, DateTime, Boolean
from database import Base
from sqlalchemy import String
import datetime


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100))


class Token(Base):
    __tablename__ = "tokens"

    user_id = Column(Integer)
    access_token = Column(String(450), primary_key=True)
    refresh_token = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    related_user_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)