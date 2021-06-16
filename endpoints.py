# from typing import List
from typing import List

from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

import services
import schemas
from database import get_db

router = APIRouter()


@router.get(
    "/projects",
    tags=["projects"],
    response_model=List[schemas.Project],
    status_code=status.HTTP_200_OK,
)
def get_projects(db: Session = Depends(get_db)):
    projects = services.get_projects(db)
    return projects


@router.get(
    "/projects/{project_id}",
    tags=["projects"],
    response_model=schemas.ProjectFull,
    status_code=status.HTTP_200_OK,
)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = services.get_project(db, project_id)
    if not project:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"Project with project_id {project_id} not found!",
        )
    return project


@router.post(
    "/projects",
    tags=["projects"],
    response_model=schemas.ProjectFull,
    status_code=status.HTTP_201_CREATED,
)
def add_project(project_in: schemas.ProjectFull, db: Session = Depends(get_db)):
    project = services.get_project(db, project_in.project_id)
    if project:
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            detail=f"Project {project_in.project_id} already exists!",
        )
    created_project = services.add_project(db, project_in)

    return created_project




@router.get(
    "/projects/{project_id}/locations",
    tags=["locations"],
    response_model=List[schemas.Location],
    status_code=status.HTTP_200_OK,
)
async def get_locations_in_project(
    project_id: int, db: Session = Depends(get_db)
):
    project = services.get_project(db, project_id)
    if not project:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"Project with project_id {project_id} not found!",
        )

    locations = services.get_locations_for_project(db, project_id)
    return locations
