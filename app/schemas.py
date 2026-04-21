from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    email: Optional[str] = None
    phone_number: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    description: str
    owner_id: int

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True
        
class UserWithTasks(UserResponse):
    id: int
    name: str
    tasks: List[TaskResponse] = []

    class Config:
        orm_mode = True