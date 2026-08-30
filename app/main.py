import uvicorn
from fastapi import FastAPI
from app.core.config import settings
from app.apis.routes.user import router as users_router

app = FastAPI(title=settings.app_name)


app.include_router(
  users_router,
  prefix="/api/v1"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

# if __name__ == "__main__":
#   # Specify your custom port here
#   uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True, app_dir="app")
