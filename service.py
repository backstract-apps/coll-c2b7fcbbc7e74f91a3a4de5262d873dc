from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_students(db: Session):

    Students_all = db.query(models.Students).all()
    Students_all = [new_data.to_dict() for new_data in Students_all] if Students_all else Students_all

    res = {
        'Students_all': Students_all,
    }
    return res

async def get_students_student_id(db: Session, student_id: int):

    Students_one = db.query(models.Students).filter(models.Students.student_id == student_id).first() 
    Students_one = Students_one.to_dict() if Students_one else Students_one

    res = {
        'Students_one': Students_one,
    }
    return res

async def post_students(db: Session, raw_data: schemas.PostStudents):
    student_id:str = raw_data.student_id
    name:str = raw_data.name
    email:str = raw_data.email
    address:str = raw_data.address


    record_to_be_added = {'student_id': student_id, 'name': name, 'email': email, 'address': address}
    new_Students = models.Students(**record_to_be_added)
    db.add(new_Students)
    db.commit()
    db.refresh(new_Students)
    Students_inserted_record = new_Students.to_dict()

    res = {
        'Students_inserted_record': Students_inserted_record,
    }
    return res

async def put_students_student_id(db: Session, raw_data: schemas.PutStudentsStudentId):
    student_id:str = raw_data.student_id
    name:str = raw_data.name
    email:str = raw_data.email
    address:str = raw_data.address


    Students_edited_record = db.query(models.Students).filter(models.Students.student_id == student_id).first()
    for key, value in {'student_id': student_id, 'name': name, 'email': email, 'address': address}.items():
          setattr(Students_edited_record, key, value)
    db.commit()
    db.refresh(Students_edited_record)
    Students_edited_record = Students_edited_record.to_dict() 

    res = {
        'Students_edited_record': Students_edited_record,
    }
    return res

async def delete_students_student_id(db: Session, student_id: int):

    Students_deleted = None
    record_to_delete = db.query(models.Students).filter(models.Students.student_id == student_id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        Students_deleted = record_to_delete.to_dict() 

    res = {
        'Students_deleted': Students_deleted,
    }
    return res

async def get_users(db: Session):

    Users_all = db.query(models.Users).all()
    Users_all = [new_data.to_dict() for new_data in Users_all] if Users_all else Users_all

    res = {
        'Users_all': Users_all,
    }
    return res

async def get_users_user_id(db: Session, user_id: int):

    Users_one = db.query(models.Users).filter(models.Users.user_id == user_id).first() 
    Users_one = Users_one.to_dict() if Users_one else Users_one

    res = {
        'Users_one': Users_one,
    }
    return res

async def post_users(db: Session, raw_data: schemas.PostUsers):
    user_id:str = raw_data.user_id
    username:str = raw_data.username
    email:str = raw_data.email
    role:str = raw_data.role


    record_to_be_added = {'user_id': user_id, 'username': username, 'email': email, 'role': role}
    new_Users = models.Users(**record_to_be_added)
    db.add(new_Users)
    db.commit()
    db.refresh(new_Users)
    Users_inserted_record = new_Users.to_dict()

    res = {
        'Users_inserted_record': Users_inserted_record,
    }
    return res

async def put_users_user_id(db: Session, raw_data: schemas.PutUsersUserId):
    user_id:str = raw_data.user_id
    username:str = raw_data.username
    email:str = raw_data.email
    role:str = raw_data.role


    Users_edited_record = db.query(models.Users).filter(models.Users.user_id == user_id).first()
    for key, value in {'user_id': user_id, 'username': username, 'email': email, 'role': role}.items():
          setattr(Users_edited_record, key, value)
    db.commit()
    db.refresh(Users_edited_record)
    Users_edited_record = Users_edited_record.to_dict() 

    res = {
        'Users_edited_record': Users_edited_record,
    }
    return res

async def delete_users_user_id(db: Session, user_id: int):

    Users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.user_id == user_id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        Users_deleted = record_to_delete.to_dict() 

    res = {
        'Users_deleted': Users_deleted,
    }
    return res

