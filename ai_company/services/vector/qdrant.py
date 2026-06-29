import os
from qdrant_client import QdrantClient
from loguru import logger

class QdrantService:

    def connect(self):

        client = QdrantClient(
            host=os.getenv("QDRANT_HOST"),
            port=int(os.getenv("QDRANT_PORT"))
        )

        client.get_collections()

        logger.success("Qdrant connected")

        return client
