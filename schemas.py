from typing import Optional, List

from pydantic import BaseModel


class Location(BaseModel):
    location_id: Optional[int]
    name: Optional[str]

    class Config:
        orm_mode = True


class Project(BaseModel):
    project_id: int
    name: Optional[str]
    srid: int
    locations: Optional[List[Location]] = []

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "project_id": 19001234,
                "name": "Project Name",
                "srid": 3857,
                "heavy": "Very big data blob!",
            }
        }


class ProjectFull(Project):
    heavy: Optional[str]
