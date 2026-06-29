from fastapi import FastAPI

app = FastAPI(title="AI Company")

@app.get("/")
def root():
    return {
        "status": "running",
        "platform": "AI Company",
        "version": "0.1"
    }
