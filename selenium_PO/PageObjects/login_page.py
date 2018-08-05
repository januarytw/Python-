class LoginPage:

    #输入框
    login_user_xpath = '//input[@name="phone"]'
    #密码输入框
    login_password_xpath = '//input[@name="password"]'
    #按钮
    login_button_xpath =  '//button'

    def __init__(self,driver):
        self.driver = driver

    def login(self):
        #打开网址
        self.driver.get(url)

        #登录
        self.driver.find_element_by_xpath(self.login_user_xpath]').send_keys(uid)
        self.driver.find_element_by_xpath(self.login_password_xpath).send_keys(pwd)
        self.driver.find_element_by_tag_name(self.login_button_xpath).click()