# -*- coding: utf-8 -*-
#参考：深圳-超人的邮件发送代码

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class SendEmail():
    def __init__(self,username,passwd,receivers,title,content,file,email_host='smtp.qq.com',port=465):
        self.username=username
        self.passwd=passwd
        self.receivers=receivers
        self.title=title
        self.content=content
        self.file=file
        self.email_host=email_host
        self.port=port
    def send_mail(self):
        msg = MIMEMultipart()
        # 发送内容的对象
        if self.file:  #处理附件的
            att = MIMEText(open(self.file,'rb').read(), 'html', 'utf-8')#open()要带参数'rb'则附件打开乱码
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="%s"' % self.file
            msg.attach(att)
        msg.attach(MIMEText(self.content))  #邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = self.receivers  # 接收者账号列表
        self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.port)
        #发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.receivers, msg.as_string())
        except Exception as e:
            print('出错了', e)
        else:
            print('发送成功')
if __name__ == '__main__':
    m = SendEmail(
        username='20044361@qq.com', passwd='ywlejecyxesbcbdf', receivers='1871949595@qq.com',
        title='HTTP日志', content='HTTP测试报告0730', file='../test_result/log/test_log.txt'
    )
    m.send_mail()
