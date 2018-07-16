#实现http请求测试的类

import unittest

from common.do_excel import DoExcel#引用时要加入common，要不然在run执行的时候这里会说找不到DoEXCEL
from common.read_config import ReadConfig
from common.http_request import HttpRequest
from common.my_log import MyLog
from ddt import ddt,data
from conf import project_path
from common.do_mysql import DoMysql

#用例的执行模式
mode=ReadConfig(project_path.case_conf_path).getConfig('CASE','mode')
case_list=eval(ReadConfig(project_path.case_conf_path).getConfig('CASE','case_list'))#！！！此处需要EVAL转换一下，要不然会在读取部分用例时，遍历case_list时报错
# print(mode,case_list)


#COOKIES全局变量
COOKIES=None

#读取到的测试数据
test_data=DoExcel(project_path.test_data_path,'test_data').read_data(mode,case_list)
ip=ReadConfig(project_path.config_conf_path).getConfig("HTTP","ip")
# print('test_date:',test_data)
#创建Log实例
logger=MyLog()


@ddt
class TestHttpRequest(unittest.TestCase):#!!!这里要继承TestCase
    def setUp(self):
        #创建操作excel的实例
        self.t=DoExcel(project_path.test_data_path,'test_data')
        logger.info("开始测试")


    @data(*test_data)
    def test_http_request(self,a):
        logger.info("测试数据是："+str(a))#!!!括号中不能用逗号的方式传递变量值
        logger.info("目前正在执行第%s条用例"%a[0])

        global COOKIES

        logger.info("请求的地址为：%s"%(ip+a[4]))
        logger.info("请求的参数为：%s"%a[5])
        print('a5的类型',type(a[5]))
        res=HttpRequest(ip+a[4],(a[5])).httpRequest(a[3],cookies=COOKIES)#!!!要将从excel中读出的字典格式装换一下
        if res.cookies!={}:#判断cookies是否为空用{},或用len(res.cookies)==0
            COOKIES=res.cookies
        # print(res.json())

        #检查数据库的值
        sql_result=DoMysql().do_mysql(a[7]['sql'],(str(a[7]['sql_data']),))
        try:
            self.assertEqual(str(sql_result),a[7]['expected'])
            check_sql_result='PASS'
        except AssertionError as e:
            check_sql_result='FAIL'
            raise e
        finally:
            self.t.write_data(a[0]+1,2,str(sql_result),check_sql_result)

        #检查excel中的预期值
        try:
            self.assertEqual(str(a[6]),res.json()['code'])#!!!预期结果要转换成str
            result='PASS'
        except AssertionError as e:
            logger.error("断言报错信息是%s"%e)
            result='FAIL'
            raise e#!!!终止后面的代码
        finally:
            self.t.write_data(a[0]+1,1,str(res.json()),result)

    def tearDown(self):
        logger.info("测试结束")