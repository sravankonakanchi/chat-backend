from .producer import _TOPIC_STORE_EXPORT

def consume_topic(topic: str):
    events = _TOPIC_STORE_EXPORT.get(topic, [])
    for e in events:
        print(f"[Consumer] Processing {topic} event={e}")
