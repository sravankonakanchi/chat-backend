from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ThreadCreate(BaseModel):
    title: str

class ThreadResponse(BaseModel):
    id: int
    title: str
    created_at: datetime

    class Config:
        orm_mode = True

class MessageCreate(BaseModel):
    thread_id: int
    sender: str
    content: str
    parent_id: Optional[int] = None

class MessageResponse(BaseModel):
    id: int
    thread_id: int
    sender: str
    content: str
    parent_id: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True
