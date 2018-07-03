#实现http请求测试的类

import unittest
from http_request import HttpRequest
from do_excel import DoExcel
from read_config import ReadConfig
from my_log import MyLog
from ddt import ddt,data

#读取到的测试数据
test_data=DoExcel('../test_data/test_case.xlsx','test_data').read_data()
# print(test_data)

#创建读取配置文件实例
rc=ReadConfig("../conf/config.conf")

#创建Log实例
name="andy"
state=rc.getConfig('LOG','state')
level=rc.getConfig('LOG','level')
formatStr=rc.getConfig('LOG','formatter')
out_file_path=rc.getConfig('LOG','out_file_path')
logger=MyLog().myLog(name,state,level,formatStr,out_file_path)

COOKIES=None#全局变量

@ddt
class TestHttpRequest(unittest.TestCase):#!!!这里要继承TestCase
    def setUp(self):
        #创建操作excel的实例
        self.t=DoExcel('../test_data/test_case.xlsx','test_data')
        logger.info("开始测试")


    @data(*test_data)
    def test_http_request(self,a):
        logger.info("测试数据是："+str(a))#!!!括号中不能用逗号的方式传递变量值
        logger.info("目前正在执行第%s条用例"%a[0])

        global COOKIES
        ip=rc.getConfig("HTTP","ip")

        logger.info("请求的地址为：%s"%(ip+a[4]))
        logger.info("请求的参数为：%s"%a[5])

        res=HttpRequest(ip+a[4],eval(a[5])).httpRequest(a[3],cookies=COOKIES)#!!!要将从excel中读出的字典格式装换一下
        if res.cookies!={}:#判断cookies是否为空用{},或用len(res.cookies)==0
            COOKIES=res.cookies
        # print(res.json())
        try:
            self.assertEqual(str(a[6]),res.json()['code'])#!!!预期结果要转换成str
            result='PASS'
        except AssertionError as e:
            logger.error("断言报错信息是%s"%e)
            result='FAIL'
            raise e#!!!终止后面的代码
        finally:
            self.t.write_data(a[0]+1,str(res.json()),result)

    def tearDown(self):
        logger.info("测试结束")