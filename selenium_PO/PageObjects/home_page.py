# 创建时间：2018/8/6 11:39

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePage:
    #用户昵称
    usernameXpath = '//a[@href="/Member/index.html"]'
    #抢投标按钮
    bid_xpath='//a[text()="抢投标"]'

    def __init__(self, driver):
        self.driver = driver
        pass

    def get_nickname(self):
        WebDriverWait(self.driver, 20, 1).until(EC.visibility_of_element_located((By.XPATH,self.usernameXpath)))
        return self.driver.find_element_by_xpath(self.usernameXpath).text


    def click_firstBib(self):
        #等待
        WebDriverWait(self.driver, 20, 1).until(EC.visibility_of_element_located(By.XPATH,self.bid_xpath))
        #找到元素
        ele = self.driver.find_element_by_xpath(self.bid_xpath)
        #滚到可见区域
        self.driver.execute_script("arguments[0].scrollIntoView()",ele)
        #点击它
        ele.click()