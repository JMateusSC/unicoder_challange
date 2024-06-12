from fastapi import APIRouter
import schemas
import models
from sqlalchemy.orm import Session
from utils import *
from fastapi import Depends, HTTPException, status
from models import User, Token
from auth_bearer import JWTBearer
from commom import get_session, token_required


router = APIRouter(prefix="/api/user", tags=["Users"])


@router.post("/register")
async def register_user(user: schemas.UserCreate, session: Session = Depends(get_session)):
    existing_user = session.query(models.User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    encrypted_password = get_hashed_password(user.password)
    new_user = models.User(username=user.username, email=user.email, password=encrypted_password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message": "User created successfully"}


@router.post('/login', response_model=schemas.TokenSchema)
async def login(request: schemas.Requestdetails, session: Session = Depends(get_session)):
    user = session.query(User).filter(User.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email")
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")

    access = create_access_token(user.id)
    refresh = create_refresh_token(user.id)
    token_db = models.Token(user_id=user.id, access_token=access, refresh_token=refresh, status=True)
    session.add(token_db)
    session.commit()
    session.refresh(token_db)
    return {"access_token": access, "refresh_token": refresh}


@router.post('/change-password')
@token_required
async def change_password(request: schemas.Changepassword, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    user = session.query(models.User).filter(models.User.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")

    if not verify_password(request.old_password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid old password")

    encrypted_password = get_hashed_password(request.new_password)
    user.password = encrypted_password
    session.commit()
    return {"message": "Password changed successfully"}


@router.post('/logout')
@token_required
async def logout(dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = jwt.decode(token, JWT_SECRET_KEY, ALGORITHM)
    user_id = payload['sub']
    token_record = session.query(models.Token).all()
    info = [record.user_id for record in token_record]
    if info:
        session.query(models.Token).filter(Token.user_id.in_(info)).delete()
        session.commit()

    existing_token = session.query(models.Token).filter(models.Token.user_id == user_id, models.Token.access_token == token).first()
    if existing_token:
        existing_token.status = False
        session.add(existing_token)
        session.commit()
        session.refresh(existing_token)
    return {"message": "Logout Successfully"}
