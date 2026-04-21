from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=schemas.UserResponse)
def create_user_endpoint(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users", response_model=List[schemas.UserResponse])
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.delete("/users/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)   

@app.put("/users/{user_id}")
def update_user_endpoint(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user)

@app.get("/users/{user_id}")
def find_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return crud.find_user(db, user_id)

@app.get("/users_with_tasks", response_model=List[schemas.UserWithTasks])
def get_users_with_tasks(db: Session = Depends(get_db)):
    return crud.get_users_with_tasks(db)

@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task_endpoint(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def find_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    return crud.find_task(db, task_id)

@app.get("/users/{user_id}/tasks", response_model=schemas.UserWithTasks)
def get_tasks(user_id: int, db: Session = Depends(get_db)):
    return crud.get_users_with_tasks(db, user_id)