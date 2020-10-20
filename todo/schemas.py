from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoBase(BaseModel):
    """
    this is common model for request nd response
    """
    title: str
    description: Optional[str] = None
    status: Optional[str] = "ongoing"


class TodoCreate(TodoBase):
    """
    this is model for request or creating todos
    """
    pass


class TodoShow(TodoBase):
    """
    this is model for response or geting todos
    """
    id: str
    added: datetime
    updated: datetime

    class Config:
        orm_mode = True
