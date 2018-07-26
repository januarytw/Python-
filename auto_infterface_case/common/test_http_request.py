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
#！！！此处需要EVAL转换一下，要不然会在读取部分用例时，遍历case_list时报错
case_list=eval(ReadConfig(project_path.case_conf_path).getConfig('CASE','case_list'))
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
        logger.info("测试数据是：{0}".format(a))#!!!括号中不能用逗号的方式传递变量值
        logger.info("目前正在执行第%s条用例"%a['case_id'])

        global COOKIES

        logger.info("请求的地址为：%s"%(ip+a['url']))
        logger.info("请求的参数为：%s"%a['params'])
        # print('a5的类型',type(a[5]))

        #此方法是针对list形式
        # res=HttpRequest(ip+a[4],(a[5])).httpRequest(a[3],cookies=COOKIES)
        #此方法是针对字典取值，可以根据key取value值
        res=HttpRequest(ip+a['url'],eval(a['params'])).httpRequest(a['method'],cookies=COOKIES)

        if res.cookies!={}:#判断cookies是否为空用{},或用len(res.cookies)==0
            COOKIES=res.cookies
        # print(res.json())

        #检查数据库的值
        # sql_result=DoMysql().do_mysql(a[7]['sql'],(str(a[7]['sql_data']),))

        #判断是否对数据库进行检查
        if a['check_sql']!=None:#是否需要对数据库进行检查
            sql_result=DoMysql().do_mysql(eval(a['check_sql'])['sql'])
            try:
                self.assertEqual(eval(a['check_sql'])['expected'],str(sql_result))#！！！a['check_sql]['expected'] 这种用法错误，应将前面转换成字典类型
                check_sql_result='PASS'
            except AssertionError as e:
                check_sql_result='FAIL'
                raise e
            finally:
                self.t.write_data(int(a['case_id'])+1,2,str(sql_result),check_sql_result)


        #判断是否存在id和regtime需要替换
        if a['expect_result'].find("${id}")!=-1 and a['expect_result'].find('${regtime}')!=-1:
            #获取手机号 从params里面去获取手机号
            mobilephone=eval(a['params'])['mobilephone']#!!! 记住，字典的键值要用“”
            #替换id
            member_id=DoMysql().do_mysql('select id from member where mobilephone=%s'%mobilephone)[0]#sql返回是元组类型
            #替换regtime
            regtime=DoMysql().do_mysql('select regtime from member where mobilephone='+mobilephone)[0]

            expected_result=eval(a['expect_result'])
            expected_result['data']['id']=member_id
            expected_result['data']['regtime']=str(regtime)+'.0'
        else:
            expected_result=eval(a['expect_result'])



        #检查excel中的预期值
        try:
            self.assertEqual(expected_result,res.json())#!!!预期结果要转换成str
            result='PASS'
        except AssertionError as e:
            logger.error("断言报错信息是%s"%e)
            result='FAIL'
            raise e#!!!终止后面的代码
        finally:
            self.t.write_data(int(a['case_id'])+1,1,str(res.json()),result)

    def tearDown(self):
        logger.info("测试结束")