import psycopg
from loguru import logger

from ai_company.core.config import config

class PostgresService:

    def connect(self):

        self.conn = psycopg.connect(

            host=config.POSTGRES_HOST,
            port=config.POSTGRES_PORT,
            dbname=config.POSTGRES_DB,
            user=config.POSTGRES_USER,
            password=config.POSTGRES_PASSWORD,

        )

        logger.success("PostgreSQL connected")

        return self.conn
