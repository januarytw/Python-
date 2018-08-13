# 创建时间：2018/8/13 15:06
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_eleVisible(self,locator,by=By.XPATH,wait_times=30):
        #判断这个by是否在8种定位方式之中

        #logging  等待xx元素可见：locator，by

        t1 = time.time()
        try:
            WebDriverWait(self.driver,wait_times,1).until(EC.visibility_of_element_located((by,locator)))
            t2 = time.time()
            #loggin 等待晚上，元素已可见t2-t1差值---等待时间
        except TimeoutError as e:
            #logging它的异常信息
            #截图
            raise e

    #当元素可见时，查找元素
    def get_element(self,locator,by=By.XPATH,wait_times=30):
        #logging 查找元素XXX
        #等待元素可见
        self.wait_eleVisible(locator,by,wait_times)
        #查找它
        try:
            ele = self.driver.find_element(by,locator)
            #logging 找到元素
            return ele
        except Exception as e:
            #logging 异常信息
            #截图
            raise e

    def get_elements(self):
        pass

    def scroll_intoView(self,ele):
        #logging 滚动
        self.driver.execute_script("arguments[0].scrollIntoView()",ele)

    def click(self,ele):
        #logging 点击操作
        try:
            ele.click()
        except Exception as e:
            #日志
            #截图
            raise e

    def send_keys(self):
        pass

    def save_screenshot(self):
        pass

    def handle_alert(self):
        pass

    def upload(self):
        pass

    def get_element_attrite(self):
        pass

    def get_text(self):
        pass