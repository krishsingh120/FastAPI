import uvicorn
from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.app_name)

@app.get("/health")
def health():
  return {
    "status": "ok",
    "app": settings.app_name
  }


# if __name__ == "__main__":
#   # Specify your custom port here
#   uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True, app_dir="app")
