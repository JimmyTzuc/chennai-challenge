import pika
import os

# variables
USER = os.getenv('RMQ_USER', 'guest')
PASSWORD = os.getenv('RMQ_PASSWORD', 'guest')
PORT = os.getenv('RMQ_PORT', 5672)
QUEUE = os.getenv('RMQ_QUEUE', 'hello')

# Connection parameters
credentials = pika.PlainCredentials(USER, PASSWORD)
parameters = pika.ConnectionParameters('localhost', PORT, '/', credentials)

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue=QUEUE)

# Fetch a single message from the queue
method_frame, header_frame, body = channel.basic_get(queue='hello', auto_ack=True)

if method_frame:
    # Print the recived message
    print(body.decode())
else:
    print("No message in the queue")

# Close the connection
connection.close()