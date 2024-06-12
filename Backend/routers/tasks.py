from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
from auth_bearer import JWTBearer, decodeJWT
import schemas
from commom import get_session, token_required


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get('/get_all')
@token_required
async def get_tasks(dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    tasks = session.query(models.Product).filter(models.Product.related_user_id == user_id).all()
    return tasks


@router.get('/get/{task_id}')
@token_required
async def get_task_by_id(task_id: int, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    existing_task = session.query(models.Task).filter(models.Task.id == task_id).first()
    if existing_task is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task not found")
    
    if (existing_task.related_user_id != user_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return existing_task


@router.post('/create')
@token_required
async def create_task(task: schemas.TaskCreate, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    new_task = models.Task(name=task.name, description=task.description, related_user_id=user_id, price=task.price)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return {"message": "Task created successfully"}


@router.put('/update')
@token_required
async def update_task(task: schemas.TaskUpdate, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    existing_task = session.query(models.Task).filter(models.Task.id == task.id).first()
    if existing_task is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task not found")

    if existing_task.related_user_id != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    existing_task.name = task.name
    existing_task.description = task.description
    existing_task.price = task.price
    session.commit()
    return {"message": "Task updated successfully"}


@router.patch('/update_partial')
@token_required
async def update_partial_task(task: schemas.TaskFetch, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    existing_task = session.query(models.Task).filter(models.Task.id == task.id).first()
    if existing_task is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task not found")

    if existing_task.related_user_id != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    if task.name:
        existing_task.name = task.name
    
    if task.description:
        existing_task.description = task.description

    if task.price:
        existing_task.price = task.price

    session.commit()
    return {"message": "Task updated successfully"}


@router.delete('/delete/{task_id}')
@token_required
async def delete_task_by_id(task_id: int, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    query_result = session.query(models.Task).filter(models.Task.id == task_id)
    if query_result.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task not found")

    if query_result.first().related_user_id != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    query_result.delete()
    session.commit()

    return {"message": "Task deleted successfully"}