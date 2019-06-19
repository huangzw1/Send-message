import pika
import sys
import json
import os
rabbitmqhost = os.environ.get('RABBITMQHOST')

credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="10.10.14.31", port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='messageq', durable=True)

# message1 = {
#     "engine": "email",
#     "content": "just for test",
#     "subject": "测试邮件",
#     "mailhost": "smtp.qq.com",
#     "mailport": 465,
#     "sender": "592750654@qq.com",
#     "password": "sbndswrkrjvrbfib",
#     "receiver": "zewei.huang@cloudtogo.cn"
# }


for i in range(10000):
    message1 = {
        "engine": "dd",
        "notice": "### test11111",
        "mstype": "markdown",
        "title": "test",
        "ddtoken": "bbd9fe6590f980153c9f929e66c2037fe42cc8b2b46c4323c12273451c96b015",
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
