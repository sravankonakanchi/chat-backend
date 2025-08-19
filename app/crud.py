from sqlalchemy.orm import Session
from . import models, schemas
from .producer import producer

def create_thread(db: Session, thread: schemas.ThreadCreate):
    db_thread = models.Thread(title=thread.title)
    db.add(db_thread)
    db.commit()
    db.refresh(db_thread)

    # Publish event
    producer.send_thread_created(db_thread.id, db_thread.title, db_thread.created_at)
    return db_thread

def get_thread(db: Session, thread_id: int):
    return db.query(models.Thread).filter(models.Thread.id == thread_id).first()

def create_message(db: Session, message: schemas.MessageCreate):
    db_msg = models.Message(
        thread_id=message.thread_id,
        sender=message.sender,
        content=message.content,
        parent_id=message.parent_id
    )
    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)

    # Publish event
    producer.send_message_created(
        db_msg.id, db_msg.thread_id, db_msg.sender, db_msg.content,
        db_msg.parent_id, db_msg.created_at
    )
    return db_msg

def get_message(db: Session, message_id: int):
    return db.query(models.Message).filter(models.Message.id == message_id).first()
