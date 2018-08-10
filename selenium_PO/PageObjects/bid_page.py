# 创建时间：2018/8/7 16:53

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BidPage:

    #金额输入框
    invest_moneyInput_xpath='//input[@class="form-control invest-unit-investinput"]'
    #投资按钮
    invest_moneySubmit_xpath='//button[text()="投标"]'
    #弹出框-查看并激活-按钮
    invest_success_activeButton_xpath='//div[@class="layui-layer-content"]//button'#另一种方法//div[contains(@class,"layui-layer-page")]//button
    #投资失败-弹出框-提示信息
    invest_failed_popup_xpath='//div[contains(@class,"layui-layer-dialog")]//div[@class="text-center"]'


    def __init__(self,driver):
        self.driver = driver

    #获取用户余额
    def get_userLeftMoney(self):
        #等待
        WebDriverWait(self.driver,20,1).until(EC.visibility_of_element_located((By.XPATH,self.invest_moneyInput_xpath)))
        #获取金额输入框的data-amount的属性值
        return self.driver.find_element_by_xpath(self.invest_moneyInput_xpath).get_attribute("data-amount")

    #投资-投资的金额
    def invest(self,money):
        pass

    #投资成功的弹出框-点击查看并激活按钮-进入个人页面
    def click_button_on_investSuccessPopup(self):
        pass



