# 创建时间：2018/8/6 11:39

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePage:

    usernameXpath = '//a[@href="/Member/index.html"]'

    def __init__(self,driver):
        self.driver = driver
        pass

    def get_nickname(self):
        WebDriverWait(self.driver, 20, 1).until(EC.visibility_of_element_located(By.XPATH,self.usernameXpath))
        return self.driver.find_element_by_xpath(self.usernameXpath).text
