import os
import redis
from loguru import logger

class RedisService:

    def connect(self):

        client = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=int(os.getenv("REDIS_PORT"))
        )

        client.ping()

        logger.success("Redis connected")

        return client
