from ai_company.bootstrap.platform import bootstrap
from ai_company.core.services.manager import service_manager
from ai_company.core.health.checker import HealthChecker

checker = HealthChecker()

def initialize():

    bootstrap()

    for name, service in service_manager.services.items():
        checker.check(name, service)
