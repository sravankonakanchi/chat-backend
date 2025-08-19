from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/threads", tags=["threads"])

@router.post("/", response_model=schemas.ThreadResponse)
def create_thread(thread: schemas.ThreadCreate, db: Session = Depends(database.get_db)):
    return crud.create_thread(db, thread)

@router.get("/{thread_id}", response_model=schemas.ThreadResponse)
def get_thread(thread_id: int, db: Session = Depends(database.get_db)):
    db_thread = crud.get_thread(db, thread_id)
    if not db_thread:
        raise HTTPException(status_code=404, detail="Thread not found")
    return db_thread
