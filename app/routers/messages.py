from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/messages", tags=["messages"])

@router.post("/", response_model=schemas.MessageResponse)
def create_message(message: schemas.MessageCreate, db: Session = Depends(database.get_db)):
    return crud.create_message(db, message)

@router.get("/{message_id}", response_model=schemas.MessageResponse)
def get_message(message_id: int, db: Session = Depends(database.get_db)):
    db_msg = crud.get_message(db, message_id)
    if not db_msg:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_msg
