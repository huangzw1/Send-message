import requests, json

data = {
    "content": "just for test",
    "subject": "测试邮件",
    "mailhost": "smtp.qq.com",
    "sender": "592750654@qq.com",
    "password": "sbndswrkrjvrbfib",
    "receiver": "zewei.huang@cloudtogo.cn"
}
data2 = {
    "notice": "### test",
    "mstype": "markdown",
    "title": "test",
    "ddtoken": "bbd9fe6590f980153c9f929e66c2037fe42cc8b2b46c4323c12273451c96b015"
}
url1 = "http://127.0.0.1:5000/email/"
url2 = "http://127.0.0.1:5000/dingding/"


r = requests.post(url2, data=data2)
print(r.text)
# print(r.json())
