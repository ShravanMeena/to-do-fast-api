from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from todo import (
    schemas, 
    models, 
    database, 
    handlers
)

# creating all the the table in database
models.Base.metadata.create_all(bind=database.engine)

# createing instance for fast api server api
app = FastAPI()

# connecting to the database
def get_db():
    db=database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todos/", response_model = schemas.TodoShow)
def create_todo(todo:schemas.TodoCreate, db:Session = Depends(get_db)):
    """
    API endpoint to create todo 
    """
    if todo is None:
        raise HTTPException(status_code=400,detail="You need to provide todo")
    return handlers.create_todo(db, todo)


@app.get("/todo/")
def show_all_todos(skip = 0, limit= 100, db:Session = Depends(get_db)):
    """
    API endpoint to get all todos
    """
    return handlers.get_all_todos(db,skip,limit)


@app.get("/todo/{todo_id}")
def show_todo(todo_id:int, db:Session=Depends(get_db)):
    """
    API endpoint to get todo
    """
    return handlers.get_todo_by_id(db,todo_id)


@app.put("/todo/{todo_id}/", response_model = schemas.TodoShow)
def update_todo(todo_id:int, todo:schemas.TodoCreate, db:Session=Depends(get_db)):
    """
    API endpoint to update todo
    """
    return handlers.update_todo(db,todo_id,todo)


@app.delete("/todo/{todo_id}/")
def delete_todo(todo_id:int,  db:Session=Depends(get_db)):
    """
    API endpoint to delet todo
    """
    handler = handlers.delete_todo(db,todo_id)
    return "deleted succesfully"