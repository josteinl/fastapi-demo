from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.requests import Request

# Add echo=True to see what sql statements are actually run|
engine = create_engine("sqlite:///./sql_app.db?check_same_thread=False")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db(request: Request) -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()