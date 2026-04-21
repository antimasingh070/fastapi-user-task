from . import models
from sqlalchemy.orm import joinedload

def create_user(db, user):
    db_user = models.User(name=user.name, email=user.email, phone_number=user.phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db, user_id):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False

def get_users(db):
    return db.query(models.User).all()

def update_user(db, user_id, user):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db_user.phone_number = user.phone_number
        db.commit()
        db.refresh(db_user)
        return db_user
    
def find_user(db, user_id):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users_with_tasks(db, user_id=None):
    if user_id is not None:
        return db.query(models.User).filter(models.User.id == user_id).options(joinedload(models.User.tasks)).first()
    return db.query(models.User).options(joinedload(models.User.tasks)).all()

def create_task(db, task):
    db_task = models.Task(title=task.title, description=task.description, owner_id=task.owner_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def find_task(db, task_id):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def create_task_for_user(db, task, user_id):
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

