import pika
import os
import sys

# Variables
USER = os.getenv('RMQ_USER', 'guest')
PASSWORD = os.getenv('RMQ_PASSWORD', 'guest')
PORT = os.getenv('RMQ_PORT', 5672)
QUEUE = os.getenv('RMQ_QUEUE', 'hello')

# message is the argument
MESSAGE = sys.argv[1]


credentials = pika.PlainCredentials(USER, PASSWORD)
parameters = pika.ConnectionParameters('localhost', PORT, '/', credentials)

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

# Declare a queue
channel.queue_declare(queue=QUEUE)

# Publish a message to the queue
channel.basic_publish(exchange='', routing_key=QUEUE, body=MESSAGE)
print("Message sent to RabbitMQ")

# Close the connection
connection.close()
