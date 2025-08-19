from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ThreadCreatedEvent(BaseModel):
    thread_id: int
    title: str
    created_at: datetime

class MessageCreatedEvent(BaseModel):
    message_id: int
    thread_id: int
    sender: str
    content_preview: str
    parent_id: Optional[int]
    created_at: datetime
