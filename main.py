from fastapi import FastAPI

api = FastAPI(
    title="EduCore API",
    version="1.0.0"
)

@api.get("/api/health", tags=["Health"])
def health():
    return {
        "status": "online",
        "service": "EduCore API",
        "version": "1.0.0"
    }