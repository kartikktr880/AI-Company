from fastapi import APIRouter
from ai_company.platform.context import platform

router = APIRouter()

@router.get("/system")

def system():

    return {

        "postgres": platform.postgres is not None,

        "redis": platform.redis is not None,

        "qdrant": platform.qdrant is not None,

        "neo4j": platform.neo4j is not None,

        "minio": platform.minio is not None

    }
