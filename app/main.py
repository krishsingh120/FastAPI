from fastapi import FastAPI

app = FastAPI(title="User API")

@app.get("/health")
def health():
  print("OK")
  return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}


