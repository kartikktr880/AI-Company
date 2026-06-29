import os
from neo4j import GraphDatabase
from loguru import logger

class Neo4jService:

    def connect(self):

        driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"),
            auth=(
                os.getenv("NEO4J_USER"),
                os.getenv("NEO4J_PASSWORD"),
            ),
        )

        logger.success("Neo4j connected")

        return driver
