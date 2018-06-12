import requests
import time
import unittest
import HTMLTestRunnerNew
from class_0607.class_0607_2 import HttpRequest


'''测试http请求类'''
url='http://apis.juhe.cn/cook/query.php'
parm={'menu':'宫保鸡丁','key':'5c12d954b0908fc265c9ff3576fab727'}
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        print("测试开始！")

    def test_get_request(self):
        h=HttpRequest(url,data=parm)
        result=h.get_post_request('get')
        print(result)

    def test_post_request(self):
        h=HttpRequest(url,data=parm)
        result=h.get_post_request('post')
        print(result)


    def tearDown(self):
        print("测试结束！\n")

if __name__=="__main__":
    suite=unittest.TestSuite()
    # suite.addTest(TestHttpRequest("test_get_request"))
    # suite.addTest(TestHttpRequest("test_post_request"))
    loader=unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestHttpRequest))
    print(suite.countTestCases())##!!查看用例集合中有多少用例

    now = time.strftime('%Y-%m-%d_%H_%M_%S')#获取当前时间!!!
    file_path="test"+now+".html"
    with open(file_path,"wb") as file:
        runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='测试报告',description='菜谱接口测试',tester='张三')
        runner.run(suite)
