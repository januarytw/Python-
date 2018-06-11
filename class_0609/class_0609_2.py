__author__ = 'Administrator'
# unittest :python 测试用例的框架

class Add:
    def add(self,a,b):
        return  a+b

#写测试用例  unittest
import unittest#引入框架
class TestAdd(unittest.TestCase):#继承
    def setUp(self):#在执行每一条用例之前会做的初始化操作
        print("我们要执行测试用例")


    def test_add_two_possitive(self):#1 以test开头 2见名之意
        t=Add()
        result=t.add(1,2)
        print(result)

    def test_add_two_negative(self):
        t=Add()
        result=t.add(-1,-2)
        print(result)

    def tearDown(self):#执行每一条用例后会做的清除工作操作
        print("我们已经结束用例的执行了")

class TestPrint(unittest.TestCase):
    def setUp(self):
        print("开始")

    def test_print_1(self):
        print ("打印第一条")

    def test_print_2(self):
        print("打印第二条")
    def tearDown(self):
        print("结束")
if __name__=="__main__":
    unittest.main()#执行当前模块所有已test开头的用例

#结果中..代表两条用例 E代表错误  F代表失败（期望值不等于实际值）
#执行顺序：根据用例方法名ASCII编码顺序执行