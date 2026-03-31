from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate
from app.models.task import Task
from app.db.database import get_db
from app.routes.auth import get_current_user
from app.models.user import User
from typing import Optional

router = APIRouter()


@router.post("/tasks")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_task = Task(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        user_id=current_user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"message": "Task created successfully"}




@router.get("/tasks")
def get_tasks(
    status: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Task).filter(Task.user_id == current_user.id)

    
    if status:
        query = query.filter(Task.status == status)

    
    tasks = query.offset(offset).limit(limit).all()

    return tasks