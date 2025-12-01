from fastapi import FastAPI
from src.routers import analyze, health
from src.config.logger import setup_logger

app = FastAPI(
    title="Social Intelligence Agent",
    version="1.0.0"
)

# Logger
logger = setup_logger(__name__)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Social Intelligence Agent API is running"}

# Routers
app.include_router(analyze.router)
app.include_router(health.router)

# Startup event
@app.on_event("startup")
async def startup_event():
    logger.info("Social Intelligence Agent started")
