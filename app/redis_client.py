import redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

redis_client = redis.from_url(REDIS_URL, decode_responses=True)

def get_ticket_key(event_id: int) -> str:
    return f"event:{event_id}:tickets_available"

def init_ticket_counter(event_id: int, capacity: int):
    key = get_ticket_key(event_id)
    redis_client.set(key, capacity)

def try_reserve_ticket(event_id: int) -> bool:
    key = get_ticket_key(event_id)
    remaining = redis_client.decr(key)
    if remaining >= 0:
        return True
    redis_client.incr(key)
    return False

def get_available_tickets(event_id: int) -> int:
    key = get_ticket_key(event_id)
    value = redis_client.get(key)
    return int(value) if value else 0

def release_ticket(event_id: int):
    key = get_ticket_key(event_id)
    redis_client.incr(key)
