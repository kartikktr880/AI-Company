import os
import psycopg
from loguru import logger

class PostgresService:

    def connect(self):

        self.conn = psycopg.connect(
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
        )

        logger.success("PostgreSQL connected")
        return self.conn
