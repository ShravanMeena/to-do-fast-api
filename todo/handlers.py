from sqlalchemy.orm import Session

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