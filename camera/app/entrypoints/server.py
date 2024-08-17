from app.adapters.camera_adapter import Camera

from fastapi import FastAPI

camera = Camera()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello world"}

