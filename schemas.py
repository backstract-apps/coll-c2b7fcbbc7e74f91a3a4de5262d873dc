from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Students(BaseModel):
    student_id: int
    name: str
    email: str
    address: str


class ReadStudents(BaseModel):
    student_id: int
    name: str
    email: str
    address: str
    class Config:
        from_attributes = True


class Users(BaseModel):
    user_id: int
    username: str
    email: str
    role: str


class ReadUsers(BaseModel):
    user_id: int
    username: str
    email: str
    role: str
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

