from fastapi import FastAPI

from ai_company.core.startup import startup

from ai_company.api.routes.health import router as health_router
from ai_company.api.routes.system import router as system_router

app = FastAPI(title="AI Company")

app.include_router(health_router)
app.include_router(system_router)

@app.on_event("startup")
def boot():
    startup()

@app.get("/")
def root():
    return {
        "status":"running",
        "platform":"AI Company"
    }
