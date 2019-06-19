import pika
import sys
import json
import os
rabbitmqhost = os.environ.get('RABBITMQHOST')

credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="10.10.14.31", port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='messageq', durable=True)


for i in range(10000):
    message1 = {
        "engine": "dd",
        "notice": "### test11111",
        "mstype": "markdown",
        "title": "test",
        "ddtoken": "xxxxxxx",
        "id": "%d" % (i)
    }
    message = json.dumps(message1)
    channel.basic_publish(
        exchange='',
        routing_key='messageq',
        body=message,
        )
    print(" [x] Sent %r" % message)
connection.close()
