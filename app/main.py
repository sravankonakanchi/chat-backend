from fastapi import FastAPI
from . import models, database
from .routers import threads, messages

# Create DB tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Chat Backend with Threads & Kafka-like Events")

app.include_router(threads.router)
app.include_router(messages.router)

@app.get("/")
def root():
    return {"message": "Chat backend running!"}
