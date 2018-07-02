
import unittest
import time
import HTMLTestRunnerNew
from test_http_request import TestHttpRequest

suite=unittest.TestSuite()
loader=unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

now = time.strftime('%Y-%m-%d_%H_%M_%S')#获取当前时间!!!
file_path="test"+now+".html"
with open(file_path,"wb") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='测试报告',description='作文大全接口测试',tester='张三')
    runner.run(suite)