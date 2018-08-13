# 创建时间：2018/8/7 16:59

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class UserPage:

    #个人余额
    user_leftMoney = '//div[@class="per_info_ct_left"]//li[@class="color_sub"]'

    def __init__(self, driver):
        self.driver = driver

    #获取个人余额
    def get_userLeftMoney(self):
        #等待
        WebDriverWait(self.driver,20,1).until(EC.visibility_of_element_located((By.XPATH,self.user_leftMoney)))
        #滚动到可见去也
        ele = self.driver.find_element_by_xpath(self.user_leftMoney)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        #获取money
        money = self.driver.find_element_by_xpath(self.user_leftMoney).text
        #截取数字部分
        money = money.split("元")
        return money[0]

