import redis
from loguru import logger
from ai_company.core.config import config

class RedisService:

    def connect(self):

        client = redis.Redis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            decode_responses=True
        )

        client.ping()

        logger.success("Redis connected")

        return client
