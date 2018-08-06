# 创建时间：2018/8/6 10:20

import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage


class Test_Login(unittest.TestCase):


    def setUp(self):
        #打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #访问登录页面
        self.driver.get("http://120.79.176.157:8012/Index/login.html")
        pass

    def tearDown(self):
        self.driver.quit()
        pass

    def test_login_success(self):
        #输入用户名密码，点击登录
        LoginPage(self.driver).login("18684720553","python")

        #结构对比，首页当中是否用用户昵称
        self.assertEqual(HomePage(self.driver,"我的帐户[小蜜蜂96027]"))

        pass
