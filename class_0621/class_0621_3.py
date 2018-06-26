'''
发送邮件
1、组装内容 email.mime.text
2、发送邮件 smtplib
SSL:QQ邮箱需要用SMTP_SSL(加密）


'''

from email.mime.text import MIMEText
import smtplib

#组装内容
msg=MIMEText('哈哈')
msg['Subject']="6666"
msg["From"]='7777'
msg["To"]='2222'
#指定发送邮件的服务器
s=smtplib.SMTP("smtp.126.com",465)
#登录
s.login("januarytw@126.com","computers?'")
#准备发送
s.sendmail('januarytw@126.com','20044361@qq.com',msg)
#退出服务
s.quit()
