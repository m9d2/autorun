import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def sendMail(msg):
    sender = 'gaoyangyang@innjoy.me'
    mail_user = 'gaoyangyang@innjoy.me'
    receivers = ['158612783@qq.com', '70202681@qq.com', 'gaoyangyang@innjoy.me']
    # receivers = ['158612783@qq.com', 'gaoyangyang@innjoy.me']
    mail_host = 'smtp.qiye.aliyun.com'
    mail_pass = 'Ch201212'
    message = MIMEMultipart()
    p = datetime.datetime.now()
    message.attach(MIMEText(str(p), 'plain', 'utf-8'))

    filePath = 'C:\\Users\\Administrator\\Nox_share\\ImageShare\\01.png'
    att1 = MIMEText(open(filePath.encode(), 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="01.png"'
    message.attach(att1)

    message['From'] = Header(mail_user, 'utf-8')  # 发送者
    message['To'] = Header("通知", 'utf-8')  # 接收者

    subject = msg
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    sendMail('抢到了，快去支付！')
