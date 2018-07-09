
import unittest
import time
import HTMLTestRunnerNew
from common.test_http_request import TestHttpRequest
from conf import project_path
from common import send_email

suite=unittest.TestSuite()
loader=unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

now = time.strftime('%Y-%m-%d_%H_%M_%S')#获取当前时间!!!
file_name="test"+now+".html"
with open(project_path.report_path+file_name,"wb") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='测试报告',description='接口测试',tester='张三')
    runner.run(suite)

sendEmail= send_email.SendEmail(username='20044361@qq.com', passwd='ywlejecyxesbcbdf', receivers='1871949595@qq.com',
        title='HTTP日志', content='HTTP测试报告0705', file=project_path.report_path+file_name)
sendEmail.send_mail()
