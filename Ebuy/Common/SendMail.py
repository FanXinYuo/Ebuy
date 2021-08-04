import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os


def send_mail(file_new, file_log, targetpath, filelist):
    smtpserver = "smtp.qq.com"      # 发件服务器
    port = 465                      # 端口
    sender = "fanxinyu_fxy@qq.com"     # 发送端
    psw = "csqdxgexuvazebbg"        # 密码/授权码
    receiver = ["fanxinyu_fxy@qq.com"]  # 接收端

    # =========编辑邮件内容=========
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    # 定义发件人，收件人，和邮件标题
    msg = MIMEMultipart()
    msg["from"] = sender    # 发件人
    for i in receiver:
        msg["to"] = i    # 收件人
    msg["subject"] = "自动化测试报告"  # 主题

    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)    # 挂起、固定

    # 附件 html格式
    att = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="report_test.html"'
    msg.attach(att)

    # 附件 log格式
    att = MIMEText(open(file_log, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="report_test.log"'
    msg.attach(att)

    # 附件 png
    filepath = ''
    filename = ''
    #  发送多个附件的邮件，这里发送指定目录下所有文件，不管文件类型
    for fileName in filelist:
        filepath = os.path.join(targetpath, fileName)
        filename = fileName
        with open(filepath, 'rb') as f:
            part = MIMEApplication(f.read())
            part.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(part)

    # =========发送邮件=========
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())    # 发送
    smtp.quit()  # 关闭
