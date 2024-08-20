import os, json
import pika
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve environment variables
RABBITMQ_URL = os.environ.get("RABBITMQ_URL")



class RabbitMQAdapter:

    def __init__(self) -> None:

        # connect to rabbitmq

        self.params = pika.URLParameters(RABBITMQ_URL)
        self.connection = pika.BlockingConnection(self.params)

        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='videofeedservice')


    def publish_message(self, message_body):
                
                self.channel.basic_publish(exchange='',
                                    routing_key='videofeedservice',
                                    body=message_body)
            
                print(" [x] Sent 'Hello from Camera service!'")

                self.connection.close()

        