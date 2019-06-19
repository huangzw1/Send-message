from flask import Flask, request, jsonify
import send_message as SM
from flask import jsonify

app = Flask(__name__)


@app.route('/dingding/', methods=['POST'])
def sending():
    """
    json:
    {
    "notice": xxx,
    "mstype": xxx,
    "title": xxx,
    "token": xxx
    }
    """
    jsonself = request.get_json()
    notice = jsonself['notice']
    mstype = jsonself['type']
    title = jsonself['title']
    token = jsonself['ddtoken']
    SM.dingding(notice, mstype, title, token)
    return 'send dingding message'
@app.route('/email/', methods=['POST'])
def sendmail():
    """
    json:
    {
    "content": xxx,
    "mailhost": xxx,
    "mailport": xxx,
    "subject": xxx,
    "sender": xxx,
    "password": xxx,
    "receiver": xxx
    }
    """
    jsonself = request.get_json()
    content = jsonself['content']
    mailhost = jsonself['mailhost']
    mailport = jsonself['mailport']
    subject = jsonself['subject']
    sender = jsonself['sender']
    password = jsonself['password']
    receiver = jsonself['receiver']
    SM.send(content, mailhost, mailport, subject, sender, password, receiver)
    return jsonify(jsonself)

if __name__ == '__main__':
    app.run(debug=True)





