from loguru import logger

class HealthChecker:

    def check(self,name,service):

        try:

            service.connect()

            logger.success(f"{name} OK")

            return True

        except Exception as e:

            logger.error(f"{name}: {e}")

            return False
