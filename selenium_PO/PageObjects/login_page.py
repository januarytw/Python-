from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:

    #输入框
    login_user_xpath = '//input[@name="phone"]'
    #密码输入框
    login_password_xpath = '//input[@name="password"]'
    #按钮
    login_button_xpath = '//button'
    #错误提示信息
    msn_loginArea_xpath = '//div[@class="form-error-info"]'

    def __init__(self, driver):
        self.driver = driver

    def login(self,username,password):

        #登录
        self.driver.find_element_by_xpath(self.login_user_xpath).send_keys(username)
        self.driver.find_element_by_xpath(self.login_password_xpath).send_keys(password)
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    #获取错误提示信息-登录区域的，登录时有两个，没有写用户名，就获取用户名的提示，密码也是一样
    def get_errorMsn_formLoginArea(self):
        #找元素之前，就要等待!!!!
        WebDriverWait(self.driver,10,1).until(EC.visibility_of_element_located((By.XPATH,self.msn_loginArea_xpath)))
        return self.driver.find_element_by_xpath(self.msn_loginArea_xpath).text