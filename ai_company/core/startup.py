from loguru import logger

from ai_company.core.runtime import initialize
from ai_company.kernel.kernel import kernel

def startup():

    logger.info("===================================")
    logger.info("AI Company Booting")
    logger.info("===================================")

    initialize()

    kernel.boot()

    logger.success("Platform initialized")
