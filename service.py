# File: service.py
from sqlalchemy.orm import Session

from model import Project


def get_projects(db: Session):
    return db.query(Project).all()
