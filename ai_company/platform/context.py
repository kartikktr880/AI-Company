from ai_company.core.services.manager import service_manager

class PlatformContext:

    @property
    def postgres(self):
        return service_manager.get("postgres")

    @property
    def redis(self):
        return service_manager.get("redis")

    @property
    def qdrant(self):
        return service_manager.get("qdrant")

    @property
    def neo4j(self):
        return service_manager.get("neo4j")

    @property
    def minio(self):
        return service_manager.get("minio")

platform = PlatformContext()
