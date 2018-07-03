

# from auto_interface_cases.common.read_config import ReadConfig
#
# rc=ReadConfig("./conf/config.conf").getConfig("HTTP","ip")
# print(rc)


from common import read_config

rc=read_config.ReadConfig("./conf/config.conf").getConfig("HTTP","ip")
print(rc)


import unittest
import time
import HTMLTestRunnerNew

#
# from common.test_http_request import TestHttpRequest
# from common.read_config import ReadConfig
#
# suite=unittest.TestSuite()
# loader=unittest.TestLoader()
#
# suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
#
# file_path=ReadConfig("../conf/config.conf").getConfig('REPORT','file_path')
# print(file_path)
# now = time.strftime('%Y-%m-%d_%H_%M_%S')#获取当前时间!!!
# file_name="test"+now+".html"
# # with open(file_path+file_name,"wb") as file:
# #     runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='测试报告',description='接口测试',tester='张三')
# #     runner.run(suite)
