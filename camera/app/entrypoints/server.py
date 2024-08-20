from app.adapters.camera_adapter import Camera
from app.adapters.rabbitmq_adapter import RabbitMQAdapter
from dotenv import load_dotenv
import pika
import os

from fastapi import FastAPI

app = FastAPI()


rabbit = RabbitMQAdapter()

# rabbit.publish_message('Hello from Camera service!')

# starting camera module to record intruders
##camera = Camera()


@app.get("/")
async def root():
    return {"message": "hello world"}

