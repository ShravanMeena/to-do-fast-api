from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column, 
    String, 
    Integer,
    DateTime
)
from todo.database import Base

# create todo model

class Todo(Base):
    """
    create to do model    
    """
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String(255), index=True)
    added = Column(DateTime, default= datetime.now, index=True)
    updated = Column(DateTime,default= datetime.now, index=True)
    status = Column(String, index=True)
