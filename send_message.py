import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from dingtalkchatbot.chatbot import DingtalkChatbot
from tenacity import retry
import logging

file_handler = logging.FileHandler("message.log", "a", encoding='UTF-8')
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO, filename='message.log', filemode='a')

#使用钉钉机器人发送消息
def dingding(notice, mstype, title, token):
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % (token)
    xiaoding = DingtalkChatbot(webhook)
    try:
        if mstype=='markdown':
            dingres = xiaoding.send_markdown(title, text=notice)
        else:
            dingres = xiaoding.send_text(msg=notice, is_at_all=True)

        if dingres['errcode'] == 0:
            logging.info('钉钉消息发送成功, response message: %s' % (dingres))
        else:
            logging.error('钉钉消息发送失败, error message: %s' % (dingres))
    except Exception as err:
        logging.error('钉钉消息发送失败, error message: %s' % (err))

#发送邮件函数
def send(content, mailhost, mailport, subject, sender, password, receiver):
    my_sender = sender
    my_pass = password
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = formataddr(["消息通知", my_sender])
    msg['Subject'] = subject
    msg['To'] = receiver
    try:
        server = smtplib.SMTP_SSL(mailhost, mailport)
        server.set_debuglevel(1)  # 和SMTP服务器的交互信息
        server.login(my_sender, my_pass)
        logging.info('成功登录邮箱！')
    except Exception as errmes:
        logging.error('登录邮箱失败，请检查邮箱信息，error message:%s' % (errmes))
    result = True
    try:
        server.sendmail(my_sender, receiver, msg.as_string())
        logging.info('成功发送邮件！')
        server.quit()
    except Exception as err:
        result = False
        logging.error('邮件发送失败，error message:%s' % (err))


    return result

# send("just for test",
#     "smtp.qq.com",
#     465,
#     "测试邮件",
#     "592750654@qq.com",
#     "sbndswrkrjvrbfib",
#     "zewei.huang@cloudtogo.cn")





