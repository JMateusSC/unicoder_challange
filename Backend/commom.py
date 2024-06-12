# commom.py

from database import Base, engine, SessionLocal
from models import Token
from functools import wraps
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth_bearer import JWTBearer, decodeJWT


Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def token_required(func):
    @wraps(func)
    async def wrapper(*args, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session), **kwargs):
        payload = decodeJWT(dependencies)
        if payload is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

        user_id = payload['sub']
        data = session.query(Token).filter_by(user_id=user_id, access_token=dependencies, status=True).first()
        if data:
            print("Token exists")
            return await func(*args, **kwargs, dependencies=dependencies, session=session)
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token blocked")
    return wrapper
