from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate
from app.models.task import Task
from app.db.database import get_db
from app.routes.auth import get_current_user
from app.models.user import User
from typing import Optional
from fastapi import HTTPException
from app.schemas.task import TaskUpdate

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



@router.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    
    db_task = db.query(Task).filter(Task.id == task_id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    
    if db_task.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    
    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)

    return {"message": "Task updated successfully"}

@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_task = db.query(Task).filter(Task.id == task_id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    
    if db_task.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    db.delete(db_task)
    db.commit()

    return {"message": "Task deleted successfully"}