from loguru import logger

class PostgresService:

    def connect(self):

        logger.info("Connecting to PostgreSQL...")
