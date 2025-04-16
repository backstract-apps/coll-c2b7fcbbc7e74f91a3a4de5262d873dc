from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Universities(BaseModel):
    id: Any
    name: str
    country: str
    city: str
    website: str


class ReadUniversities(BaseModel):
    id: Any
    name: str
    country: str
    city: str
    website: str
    class Config:
        from_attributes = True


class Students(BaseModel):
    id: Any
    university_id: int
    first_name: str
    last_name: str
    email: str
    password_hash: str
    major: str
    enrollment_year: int
    bio: str
    profile_picture_url: str
    created_at: Any


class ReadStudents(BaseModel):
    id: Any
    university_id: int
    first_name: str
    last_name: str
    email: str
    password_hash: str
    major: str
    enrollment_year: int
    bio: str
    profile_picture_url: str
    created_at: Any
    class Config:
        from_attributes = True


class Courses(BaseModel):
    id: Any
    university_id: int
    course_code: str
    title: str
    description: str


class ReadCourses(BaseModel):
    id: Any
    university_id: int
    course_code: str
    title: str
    description: str
    class Config:
        from_attributes = True


class Projects(BaseModel):
    id: Any
    creator_student_id: int
    course_id: int
    title: str
    description: str
    status: str
    start_date: datetime.date
    end_date: datetime.date
    created_at: Any


class ReadProjects(BaseModel):
    id: Any
    creator_student_id: int
    course_id: int
    title: str
    description: str
    status: str
    start_date: datetime.date
    end_date: datetime.date
    created_at: Any
    class Config:
        from_attributes = True


class ProjectMembers(BaseModel):
    id: Any
    project_id: int
    student_id: int
    role: str
    joined_at: Any


class ReadProjectMembers(BaseModel):
    id: Any
    project_id: int
    student_id: int
    role: str
    joined_at: Any
    class Config:
        from_attributes = True


class Tasks(BaseModel):
    id: Any
    project_id: int
    assignee_student_id: int
    title: str
    description: str
    status: str
    due_date: datetime.date
    created_at: Any


class ReadTasks(BaseModel):
    id: Any
    project_id: int
    assignee_student_id: int
    title: str
    description: str
    status: str
    due_date: datetime.date
    created_at: Any
    class Config:
        from_attributes = True


class Discussions(BaseModel):
    id: Any
    project_id: int
    course_id: int
    creator_student_id: int
    title: str
    created_at: Any


class ReadDiscussions(BaseModel):
    id: Any
    project_id: int
    course_id: int
    creator_student_id: int
    title: str
    created_at: Any
    class Config:
        from_attributes = True


class Posts(BaseModel):
    id: Any
    discussion_id: int
    author_student_id: int
    content: str
    parent_post_id: int
    created_at: Any


class ReadPosts(BaseModel):
    id: Any
    discussion_id: int
    author_student_id: int
    content: str
    parent_post_id: int
    created_at: Any
    class Config:
        from_attributes = True


class Skills(BaseModel):
    id: Any
    name: str
    description: str


class ReadSkills(BaseModel):
    id: Any
    name: str
    description: str
    class Config:
        from_attributes = True


class StudentSkills(BaseModel):
    id: Any
    student_id: int
    skill_id: int
    proficiency_level: str


class ReadStudentSkills(BaseModel):
    id: Any
    student_id: int
    skill_id: int
    proficiency_level: str
    class Config:
        from_attributes = True




class PostStudents(BaseModel):
    student_id: str
    name: str
    email: str
    address: str

    class Config:
        from_attributes = True



class PutStudentsStudentId(BaseModel):
    student_id: str
    name: str
    email: str
    address: str

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    user_id: str
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True



class PutUsersUserId(BaseModel):
    user_id: str
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True

