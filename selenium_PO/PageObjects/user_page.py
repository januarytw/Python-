# 创建时间：2018/8/7 16:59

from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage


class UserPage:

    #个人余额

    def __init__(self, driver):
        self.driver = driver

    #获取个人余额
    def get_userLeftMoney(self):
        pass
