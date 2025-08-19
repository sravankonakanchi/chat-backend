import json
import uuid
from datetime import datetime
from typing import Dict, List

# In-memory topic store (simulates Kafka)
_TOPIC_STORE: Dict[str, List[dict]] = {}

class MockProducer:
    def __init__(self):
        self.store = _TOPIC_STORE

    def _emit(self, topic: str, payload: dict):
        record = {
            "metadata": {
                "event_id": str(uuid.uuid4()),
                "occurred_at": datetime.utcnow().isoformat() + "Z"
            },
            "payload": payload
        }
        self.store.setdefault(topic, []).append(record)
        print(f"[MockProducer] Topic={topic} Event={json.dumps(record)}")

    def send_thread_created(self, thread_id: int, title: str, created_at):
        payload = {"thread_id": thread_id, "title": title, "created_at": created_at.isoformat()}
        self._emit("thread.created.v1", payload)

    def send_message_created(self, message_id: int, thread_id: int, sender: str, content: str, parent_id, created_at):
        payload = {
            "message_id": message_id,
            "thread_id": thread_id,
            "sender": sender,
            "content_preview": content[:200],
            "parent_id": parent_id,
            "created_at": created_at.isoformat()
        }
        self._emit("message.created.v1", payload)

producer = MockProducer()

_TOPIC_STORE_EXPORT = _TOPIC_STORE
