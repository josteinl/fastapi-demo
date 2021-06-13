# from typing import List

from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

import service
from database import get_db
# from service import get_projects

router = APIRouter()


@router.get(
    "/projects",
    # response_model=List[schemas.Project],
    status_code=status.HTTP_200_OK,
)
def get_projects(db: Session = Depends(get_db)):
    projects = service.get_projects(db)
    return projects

