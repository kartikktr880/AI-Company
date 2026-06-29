from ai_company.services.database.postgres import PostgresService
from ai_company.services.cache.redis import RedisService
from ai_company.services.vector.qdrant import QdrantService
from ai_company.services.graph.neo4j import Neo4jService
from ai_company.services.storage.minio import MinioService

from ai_company.core.services.manager import service_manager

def bootstrap():

    service_manager.register("postgres",PostgresService())

    service_manager.register("redis",RedisService())

    service_manager.register("qdrant",QdrantService())

    service_manager.register("neo4j",Neo4jService())

    service_manager.register("minio",MinioService())
