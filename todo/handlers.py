from sqlalchemy.orm import Session
from datetime import datetime

from todo import schemas, models


def create_todo(db : Session, todo: schemas.TodoCreate):
    """
    create new todo using this handler
    """
    db_instance = models.Todo(**todo.dict())
    db.add(db_instance)
    db.commit()
    db.refresh(db_instance)
    return db_instance


def get_all_todos(db : Session, skip : int = 0, limit : int = 100):
    """
    get all todos list using this handler
    """
    return db.query(models.Todo).offset(skip).limit(limit).all()

def get_todo_by_id(db : Session, todo_id:int):
    """
    get todo by id
    """    
    db_instance = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    return db_instance


def update_todo(db: Session, todo_id:int, todo:schemas.TodoCreate):
    """
    update to do by geting by id
    """   
    db_instance = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db_instance.title = todo.title
    db_instance.description = todo.description
    db_instance.status = todo.status
    db_instance.updated = datetime.now()
    db.commit()
    db.refresh(db_instance)
    return db_instance


def delete_todo(db:Session, todo_id:int):
    """
    todo deleted
    """
    db_instance = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(db_instance)
    db.commit()
    # db.refresh(db_instance)
    return db_instance
