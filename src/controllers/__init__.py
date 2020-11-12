import redis

from src.settings import CACHE_HOST

redis_client = redis.Redis(host=CACHE_HOST, port=6379, db=0)