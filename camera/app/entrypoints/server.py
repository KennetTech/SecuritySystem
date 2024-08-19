from app.adapters.camera_adapter import Camera
from app.adapters.rabbitmq_adapter import RabbitMQAdapter
from dotenv import load_dotenv
import pika
import os

from fastapi import FastAPI

app = FastAPI()

# Load environment variables
load_dotenv()

# Retrieve environment variables
RABBITMQ_URL = os.environ.get("RABBITMQ_URL")

# connect to rabbitmq
params = pika.URLParameters(RABBITMQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='videofeedservice')


# starting camera module to record intruders
##camera = Camera()


@app.get("/")
async def root():
    return {"message": "hello world"}

