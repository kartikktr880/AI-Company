from qdrant_client import QdrantClient
from loguru import logger
from ai_company.core.config import config

class QdrantService:

    def connect(self):

        client = QdrantClient(
            host=config.QDRANT_HOST,
            port=config.QDRANT_PORT,
            check_compatibility=False
        )

        client.get_collections()

        logger.success("Qdrant connected")

        return client
