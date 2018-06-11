import requests
import unittest
import HTMLTestRunnerNew

#http请求类
class HttpRequest:
    def __init__(self,url,data=None):
        self.url=url
        self.data=data

    def get_post_request(self,mothod):
        try:
            if mothod.upper()=="GET":
                response=requests.get(self.url,self.data)
                print(response.json())
            elif mothod.upper()=="POST":
                response=requests.post(self.url,self.data)
                print(response.json())
        except Exception as e:
            print ("请求失败，出现的错误是%s"%e)
            raise e


# h=HttpRequest("http://apis.juhe.cn/cook/query.php",data={'menu':'宫保鸡丁','key':'5c12d954b0908fc265c9ff3576fab727'})
# res=h.get_post_request("get")
# print(res)

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
    suite.addTest(TestHttpRequest("test_get_request"))
    suite.addTest(TestHttpRequest("test_post_request"))
    # loader=unittest.TestLoader()
    # suite.addTest(loader.loadTestsFromTestCase(HTMLTestRunnerNew))

    with open("test_report.html","wb") as file:
        runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='测试报告',description='1234567',tester='校长')
        runner.run(suite)
