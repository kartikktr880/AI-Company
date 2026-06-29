from minio import Minio

from loguru import logger

from ai_company.core.config import config

class MinioService:

    def connect(self):

        client = Minio(

            config.MINIO_ENDPOINT,

            access_key=config.MINIO_ROOT_USER,

            secret_key=config.MINIO_ROOT_PASSWORD,

            secure=False,

        )

        logger.success("MinIO connected")

        return client
