import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import models, crud, schemas
from app.database import Base
from app.producer import _TOPIC_STORE_EXPORT

# setup test db
SQLALCHEMY_TEST_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_TEST_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()

def test_create_thread_and_event(db):
    thread = crud.create_thread(db, schemas.ThreadCreate(title="Test Thread"))
    assert thread.id is not None
    assert "thread.created.v1" in _TOPIC_STORE_EXPORT

def test_create_message_and_event(db):
    thread = crud.create_thread(db, schemas.ThreadCreate(title="Another Thread"))
    msg = crud.create_message(db, schemas.MessageCreate(
        thread_id=thread.id, sender="Sravan", content="Hello"
    ))
    assert msg.id is not None
    assert "message.created.v1" in _TOPIC_STORE_EXPORT
