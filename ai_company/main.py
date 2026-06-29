from fastapi import FastAPI

from ai_company.core.bootstrap import bootstrap

bootstrap()

app = FastAPI(title="AI Company")

@app.get("/")

def root():

    return {
        "status":"running",
        "platform":"AI Company"
    }
