from fastapi import FastAPI

from routes.vision import router as vision_router
from routes.health import router as health_router

app = FastAPI(
    title="Vision",
    version="1.0.0"
)

app.include_router(vision_router)
app.include_router(health_router)


@app.get("/")
def home():

    return {

        "service":"Vision",

        "status":"running"

    }
