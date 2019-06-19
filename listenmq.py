import pika
import send_message as SM
import json
import os
import logging

file_handler = logging.FileHandler("message.log", "a", encoding='UTF-8')
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO, filename='message.log', filemode='a')

rabbitmqhost = os.environ.get('RABBITMQHOST')
# try:
credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.10.14.31', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='messageq', durable=True)
# except Exception as err:
#     logging.error('connect to rabbitmq wrong,error message:%s' % (err))

def callback(ch, method, propertites, body):
    recbody = body.decode("utf-8")
    recbody = json.loads(body)
    print(recbody)
    print(type(recbody))
    engine = recbody["engine"]
    if engine=="email":
        content = recbody["content"]
        mailhost = recbody["mailhost"]
        subject = recbody["subject"]
        mailport = recbody["mailport"]
        sender = recbody["sender"]
        password = recbody["password"]
        receiver = recbody["receiver"]
        SM.send(content, mailhost, mailport, subject, sender, password, receiver)
    elif engine=="dd":
        notice = recbody["notice"]
        title = recbody["notice"]
        mstype = recbody["mstype"]
        token = recbody["ddtoken"]
        SM.dingding(notice, mstype, title, token)
    elif engine=="emaildd":
        content = recbody["content"]
        mailhost = recbody["mailhost"]
        subject = recbody["subject"]
        mailport = recbody["mailport"]
        sender = recbody["sender"]
        password = recbody["password"]
        receiver = recbody["receiver"]
        notice = recbody["notice"]
        title = recbody["notice"]
        mstype = recbody["mstype"]
        token = recbody["ddtoken"]
        SM.send(content, mailhost, mailport, subject, sender, password, receiver)
        SM.dingding(notice, mstype, title, token)

channel.basic_qos(prefetch_count=1)  #公平分配消息
channel.basic_consume(queue='messageq', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
