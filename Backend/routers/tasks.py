from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
from auth_bearer import JWTBearer, decodeJWT
import schemas
from commom import get_session, token_required
import datetime

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])


@router.get('/get_all')
@token_required
async def get_tasks(dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    tasks = session.query(models.Task).filter(models.Task.related_user_id == user_id).all()
    return tasks


@router.get('/get/{task_id}')
@token_required
async def get_task_by_id(task_id: int, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']
    print(user_id)
    existing_task = session.query(models.Task).filter(models.Task.id == int(task_id)).first()

    print(existing_task.related_user_id)
    if existing_task is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task not found")
    
    if (int(existing_task.related_user_id) != int(user_id)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return existing_task


@router.post('/create')
@token_required
async def create_task(task: schemas.TaskCreate, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    new_task = models.Task(
        related_user_id = user_id,
        status = task.status, 
        title = task.title, 
        description = task.description, 
        dead_line = task.dead_line, 
        creation_date = task.creation_date, 
        end_date = task.end_date, 
        expected_time = task.expected_time, 
        registered_time = task.registered_time, 
    )
    
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

    existing_task = session.query(models.Task).filter(models.Task.id == int(task.id)).first()
    if existing_task is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task not found")

    if int(existing_task.related_user_id) != int(user_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    existing_task.status = task.status
    existing_task.title = task.title
    existing_task.description = task.description
    existing_task.dead_line = task.dead_line
    existing_task.end_date = task.end_date
    existing_task.expected_time = task.expected_time
    existing_task.registered_time = task.registered_time

    session.commit()
    return {"message": "Task updated successfully"}


@router.patch('/update_partial')
@token_required
async def update_partial_task(task: schemas.TaskFetch, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    existing_task = session.query(models.Task).filter(models.Task.id == int(task.id)).first()
    if existing_task is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task not found")

    if int(existing_task.related_user_id) != int(user_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    if task.status:
        existing_task.status = task.status
        if task.status == "DONE":
            existing_task.end_date = datetime.datetime.now(datetime.timezone.utc)
    if task.title:
        existing_task.title = task.title
    if task.description:
        existing_task.description = task.description
    if task.dead_line:
        existing_task.dead_line = task.dead_line
    if task.end_date:
        existing_task.end_date = task.end_date
    if task.expected_time:
        existing_task.expected_time = task.expected_time
    if task.registered_time:
        existing_task.registered_time = task.registered_time

    session.commit()
    return {"message": "Task updated successfully"}


@router.delete('/delete/{task_id}')
@token_required
async def delete_task_by_id(task_id: int, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    query_result = session.query(models.Task).filter(models.Task.id == int(task_id))
    if query_result.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task not found")

    if int(query_result.first().related_user_id) != int(user_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    query_result.delete()
    session.commit()

    return {"message": "Task deleted successfully"}