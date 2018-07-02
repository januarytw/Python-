#实现http请求测试的类

import unittest
from http_request import HttpRequest
from do_excel import DoExcel
from ddt import ddt,data

#读取到的测试数据
test_data=DoExcel('test_case.xlsx','test_data').read_data()
# print(test_data)

COOKIES=None#全局变量

@ddt
class TestHttpRequest(unittest.TestCase):#!!!这里要继承TestCase
    def setUp(self):
        #创建操作excel的实例
        self.t=DoExcel('test_case.xlsx','test_data')
        print("开始测试")

    @data(*test_data)
    def test_http_request(self,a):
        print("测试数据是：",a)
        print("目前正在执行第%s条用例"%a[0])
        global COOKIES
        res=HttpRequest(a[4],a[5]).httpRequest(a[3],cookies=COOKIES)
        if res.cookies!={}:#判断cookies是否为空用{},或用len(res.cookies)==0
            COOKIES=res.cookies
        print(res.json())
        try:
            self.assertEqual(str(a[6]),res.json()['code'])#!!!预期结果要转换成str
            result='PASS'
        except AssertionError as e:
            result='FAIL'
            raise e#!!!终止后面的代码
        finally:
            self.t.writeData(a[0]+1,str(res.json),result)

    def tearDown(self):
        print("测试结束")