# File: services.py
from sqlalchemy.orm import Session, undefer

import schemas
from model import Project, Location


def add_project(db: Session, project: schemas.ProjectFull):
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    return db_project


def get_project(db: Session, project_id):
    return db.query(Project).options(undefer('heavy')).get(project_id)


def get_projects(db: Session):
    return db.query(Project).all()


def get_locations_for_project(db, project_id):
    return db.query(Location).filter(Location.project_id == project_id).all()
