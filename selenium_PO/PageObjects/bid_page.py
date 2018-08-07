# 创建时间：2018/8/7 16:53

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BidPage:

    #金额输入框
    #投资按钮
    #弹出框-查看并激活

    def __init__(self,driver):
        self.driver = driver

    #获取用户余额
    def get_userLeftMoney(self):
        pass

    #投资-投资的金额
    def invest(self,money):
        pass

    #投资成功的弹出框-点击查看并激活按钮-进入个人页面
    def click_button_on_investSuccessPopup(self):
        pass