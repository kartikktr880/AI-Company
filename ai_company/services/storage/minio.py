import os
from minio import Minio
from loguru import logger

class MinioService:

    def connect(self):

        client = Minio(
            os.getenv("MINIO_ENDPOINT"),
            access_key=os.getenv("MINIO_ROOT_USER"),
            secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
            secure=False,
        )

        logger.success("MinIO connected")

        return client
