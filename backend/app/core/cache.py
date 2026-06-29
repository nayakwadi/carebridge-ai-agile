"""Optional Redis cache (data tier). Degrades gracefully to a no-op when Redis is down,
so tests and bare local runs never hard-depend on it."""
import json

import redis

from .config import settings

try:
    _client: redis.Redis | None = redis.Redis.from_url(
        settings.redis_url, socket_connect_timeout=1, decode_responses=True
    )
    _client.ping()
except Exception:
    _client = None


def get_json(key: str):
    if _client is None:
        return None
    try:
        raw = _client.get(key)
        return json.loads(raw) if raw else None
    except Exception:
        return None


def set_json(key: str, value, ttl_seconds: int = 15) -> None:
    if _client is None:
        return
    try:
        _client.setex(key, ttl_seconds, json.dumps(value))
    except Exception:
        pass


def available() -> bool:
    return _client is not None
