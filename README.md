# Chat Backend (FastAPI + SQLite)

This chat application is developed using FastAPI, SQLite, and SQLAlchemy.
It supports Threads (conversations) and Messages (individual
chat entries)
A mocked Kafka producer is included to simulate event publishing.

======================

# How to Run the App

1. Create a virtual environment & install dependencies:

    ''' bash
    python3 -m venv venv
    source venv/bin/activate   # Mac/Linux
    pip install -r requirements.txt
    '''

2.  Start the application:

    ''' bash
    uvicorn app.main:app --reload
    '''

    API available at: http://127.0.0.1:8000/docs

3.  Run tests:

    ''' bash
    pytest -v
    '''

==================

# Key Concepts & Architectural Decisions

-  Thread → Represents a conversation. Each thread has a title and can hold multiple messages.

-  Message → A single chat entry that belongs to a thread. Contains content, sender, and optional parent_id for replies.

-  FastAPI chosen for quick API development and built-in validation.

-  SQLite + SQLAlchemy used as lightweight database + ORM.

-  Each part has it's own job:

    models.py → database schema
    schemas.py → request/response validation
    crud.py → database operations
    routers/ → API endpoints for threads and messages
    events.py → mocked Kafka producer

-   Mocked Kafka producer - logs events for each message →
    architecture allows plugging in real Kafka later.

================

#  Kafka / Topic Thinking

-   Each new message can trigger an event published to a Kafka topic.
-   Topics: thread.created.v1, message.created.v1.
-   Producers → chat service pushes message events.
-   Consumers → Consumers (e.g., notifications, analytics, search indexing) could then process these events independently.
-   Current project mocks Kafka (logs events), but topics are
    designed so a real Kafka cluster could be dropped in with minimal
    changes.

