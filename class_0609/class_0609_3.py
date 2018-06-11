__author__ = 'Administrator'
#执行指定的测试用例
import unittest
from class_0609.class_0609_2 import TestAdd

#测试套件 存储测试用例
suite=unittest.TestSuite()

#要addTest是添加测试用例的，
# addTest参数中要求必须是一个实例
#TestAdd.test_add_two_negative()不用这样写，下面的写法其实是TestAdd的初始化函数规定的
suite.addTest(TestAdd("test_add_two_possitive"))

#加载测试用例
# loader=unittest.TestLoader()
# suite.addTests(loader.loadTestsFromModule(class_0609_2))#导入模块的所有用例，这里导入的是要注意
# suite.addTest(loader.loadTestsFromTestCase(TestAdd))#导入用例类


# with open("test_report.txt","w") as file:
# with open("test_report.html","wb") as file:
#     #下面是执行你存在suite里面的用例
#     runner=unittest.TextTestRunner(file,descriptions="这是个报告",verbosity=1)#verbosity有三个值，0.1.2
#     runner.run(suite)

runner=unittest.TextTestRunner()


# 加载类的方法：4种方法，main  suite loader模块 loader测试类 
