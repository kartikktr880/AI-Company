from fastapi import FastAPI

from ai_company.core.startup import startup
from ai_company.api.routes.health import router

app = FastAPI(title="AI Company")

app.include_router(router)

@app.on_event("startup")
def boot():
    startup()

@app.get("/")
def root():
    return {
        "status":"running",
        "platform":"AI Company"
    }
