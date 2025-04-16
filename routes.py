from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/students/')
async def get_students(db: Session = Depends(get_db)):
    try:
        return await service.get_students(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/student_id')
async def get_students_student_id(student_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_students_student_id(db, student_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/students/')
async def post_students(raw_data: schemas.PostStudents, db: Session = Depends(get_db)):
    try:
        return await service.post_students(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/students/student_id/')
async def put_students_student_id(raw_data: schemas.PutStudentsStudentId, db: Session = Depends(get_db)):
    try:
        return await service.put_students_student_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/students/student_id')
async def delete_students_student_id(student_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_students_student_id(db, student_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/user_id')
async def get_users_user_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_user_id(db, user_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/user_id/')
async def put_users_user_id(raw_data: schemas.PutUsersUserId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_user_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/user_id')
async def delete_users_user_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_user_id(db, user_id)
    except Exception as e:
        raise HTTPException(500, str(e))

