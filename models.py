from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Universities(Base):
    __tablename__ = 'universities'
    id = Column(String, primary_key=True)
    name = Column(String, primary_key=False)
    country = Column(String, primary_key=False)
    city = Column(String, primary_key=False)
    website = Column(String, primary_key=False)


class Students(Base):
    __tablename__ = 'students'
    id = Column(String, primary_key=True)
    university_id = Column(Integer, primary_key=False)
    first_name = Column(String, primary_key=False)
    last_name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    password_hash = Column(String, primary_key=False)
    major = Column(String, primary_key=False)
    enrollment_year = Column(Integer, primary_key=False)
    bio = Column(String, primary_key=False)
    profile_picture_url = Column(String, primary_key=False)
    created_at = Column(String, primary_key=False)


class Courses(Base):
    __tablename__ = 'courses'
    id = Column(String, primary_key=True)
    university_id = Column(Integer, primary_key=False)
    course_code = Column(String, primary_key=False)
    title = Column(String, primary_key=False)
    description = Column(String, primary_key=False)


class Projects(Base):
    __tablename__ = 'projects'
    id = Column(String, primary_key=True)
    creator_student_id = Column(Integer, primary_key=False)
    course_id = Column(Integer, primary_key=False)
    title = Column(String, primary_key=False)
    description = Column(String, primary_key=False)
    status = Column(String, primary_key=False)
    start_date = Column(Date, primary_key=False)
    end_date = Column(Date, primary_key=False)
    created_at = Column(String, primary_key=False)


class ProjectMembers(Base):
    __tablename__ = 'project_members'
    id = Column(String, primary_key=True)
    project_id = Column(Integer, primary_key=False)
    student_id = Column(Integer, primary_key=False)
    role = Column(String, primary_key=False)
    joined_at = Column(String, primary_key=False)


class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(String, primary_key=True)
    project_id = Column(Integer, primary_key=False)
    assignee_student_id = Column(Integer, primary_key=False)
    title = Column(String, primary_key=False)
    description = Column(String, primary_key=False)
    status = Column(String, primary_key=False)
    due_date = Column(Date, primary_key=False)
    created_at = Column(String, primary_key=False)


class Discussions(Base):
    __tablename__ = 'discussions'
    id = Column(String, primary_key=True)
    project_id = Column(Integer, primary_key=False)
    course_id = Column(Integer, primary_key=False)
    creator_student_id = Column(Integer, primary_key=False)
    title = Column(String, primary_key=False)
    created_at = Column(String, primary_key=False)


class Posts(Base):
    __tablename__ = 'posts'
    id = Column(String, primary_key=True)
    discussion_id = Column(Integer, primary_key=False)
    author_student_id = Column(Integer, primary_key=False)
    content = Column(String, primary_key=False)
    parent_post_id = Column(Integer, primary_key=False)
    created_at = Column(String, primary_key=False)


class Skills(Base):
    __tablename__ = 'skills'
    id = Column(String, primary_key=True)
    name = Column(String, primary_key=False)
    description = Column(String, primary_key=False)


class StudentSkills(Base):
    __tablename__ = 'student_skills'
    id = Column(String, primary_key=True)
    student_id = Column(Integer, primary_key=False)
    skill_id = Column(Integer, primary_key=False)
    proficiency_level = Column(String, primary_key=False)


