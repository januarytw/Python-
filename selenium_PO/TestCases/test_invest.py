# 创建时间：2018/8/7 15:20

#前置条件，已经登录，争取的账号
#确认当前用户钱够不够
#尽量少依赖测试环境--测试环境会变
#自动化测试时，要使用独立的账号，避免其他的干扰

# 步骤
'''
首页-选择第一个标的前投标按钮
标的页面，获取投资前的用户余额（用于后面期望中的比较）
标的页面，输入投资金额，进行投资操作，投资成功的弹框
'''
#期望
'''
进入个人页面，看也得的钱少了没有。投资前和投资后的钱数
投资后-个人页面里面的余额
'''

import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from PageObjects.bid_page import BidPage
from PageObjects.user_page import UserPage

from TestDatas.Common_Data import *
from TestDatas.invest_data import *

class Test_Invest(unittest.TestCase):

    def setUp(self):
        #打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #访问登录页面
        self.driver.get(url)
        LoginPage(self.driver).login(user,password)

    def tearDown(self):
        self.driver.quit()

    def test_invest_success(self):
        '''
        首页-选择第一个标的前投标按钮
        标的页面，获取投资前的用户余额（用于后面期望中的比较）
        标的页面，输入投资金额，进行投资操作，投资成功的弹框
        '''
        HomePage(self.driver).click_firstBib()
        bid_p = BidPage(self.driver)
        #获取投资之前的余额
        money_beforeInvest = bid_p.get_userLeftMoney()
        bid_p.invest(invest_1)
        bid_p.click_button_on_investSuccessPopup()

        #验证
        money_afterInvest = UserPage(self.driver).get_userLeftMoney()

        self.assertEqual(int(float(money_beforeInvest)-float(money_afterInvest)),invest_1)
