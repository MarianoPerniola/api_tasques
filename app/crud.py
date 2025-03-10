from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate


def get_tasks(db: Session):
    """
    Input:
        db: database session
    Output:
        List all tasks
    """
    # TODO: El vostre codi va aqui
    pass


def create_tasks(db: Session, task: TaskCreate):
    """
    Input:
        db: database session
    Output:
        Return the new task
    """
    # TODO: El vostre codi va aqui
    pass


def update_tasks(db: Session, task_id: int, task_update: TaskUpdate):
    """
    Input:
        db: database session
    Output:
        Updated some task fields
    """
    # TODO: El vostre codi va aqui
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        for key, value in task_update.dict(exclude_unset=True).items():
            setattr(db_task, key, value)  
        db.commit()
        db.refresh(db_task)
    return db_task

    pass


def delete_tasks(db: Session, task_id: int):
    """
    Input:
        db: database session
    Output:
        Return delete task
    """
    # TODO: El vostre codi va aqui
    db_task = db.query(Task).filter(Task.id == task_id).first() 
    if db_task:
        db.delete(db_task) 
        db.commit()
    return db_task

    pass
