from loguru import logger
from ai_company.core.runtime import initialize

def startup():

    logger.info("===================================")
    logger.info("AI Company Booting")
    logger.info("===================================")

    initialize()

    logger.success("Platform initialized")
