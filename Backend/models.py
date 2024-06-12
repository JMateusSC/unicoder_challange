from sqlalchemy import Column, Integer, DateTime, Boolean, String, Text, Float
from database import Base
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


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    related_user_id = Column(Integer)
    status = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(10000), nullable=False)
    dead_line = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    creation_date = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    end_date = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    expected_time = Column(Integer, nullable=False)
    registered_time = Column(Integer, nullable=False)
