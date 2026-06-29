from neo4j import GraphDatabase

from loguru import logger

from ai_company.core.config import config

class Neo4jService:

    def connect(self):

        driver = GraphDatabase.driver(

            config.NEO4J_URI,

            auth=(

                config.NEO4J_USER,
                config.NEO4J_PASSWORD,

            ),

        )

        logger.success("Neo4j connected")

        return driver
