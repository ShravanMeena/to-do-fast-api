from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database url 
db_url = "sqlite:///./todo.db"

# craete engine
engine = create_engine(
    db_url, 
    connect_args={"check_same_thread" : False}
)

# local session
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()