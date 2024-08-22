from app.adapters.camera_adapter import Camera

from dotenv import load_dotenv
import pika
import os

from fastapi import FastAPI

app = FastAPI()

# starting camera module to record intruders
camera = Camera()


@app.get("/")
async def root():
    return {"message": "hello world"}