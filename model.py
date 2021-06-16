from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, deferred
from sqlalchemy.sql.schema import ForeignKey

from database import Base, engine


# File: model.py


class Project(Base):
    __tablename__ = "project"
    project_id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String, nullable=True)
    srid = Column(Integer, nullable=False)
    heavy = deferred(Column(String, nullable=True))
    locations = relationship(
        "Location",
        back_populates="project",
    )


class Location(Base):
    __tablename__ = "location"
    location_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    project_id = Column(Integer, ForeignKey("project.project_id"), nullable=False)
    project = relationship("Project", back_populates="locations")


Base.metadata.create_all(engine)
