from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()


def login(url, uid, pwd):
    #打开网址
    driver.get(url)

    #登录
    driver.find_element_by_xpath('//input[@name="phone"]').send_keys(uid)
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(pwd)
    driver.find_element_by_tag_name("button").click()

#正常登录
login("http://120.79.176.157:8012/Index/login.html", "18684720553", "python")

# 验证
try:
    usernameXpath='//a[@href="/Member/index.html" and text()="我的帐户[小蜜蜂96027]"]'
    WebDriverWait(driver,20,1).until(EC.visibility_of_element_located(By.XPATH,usernameXpath))
except:
    print("没有找到用户昵称")

time.sleep(2)
driver.quit()

#不输入密码登录
login("http://120.79.176.157:8012/Index/login.html", "18684720553", "")

#验证
error_msg_xpath = "//div[@class='form-error-info']"
check_msg = "请输入密码"
WebDriverWait(driver, 20, 1).until(EC.visibility_of_element_located(By.XPATH, error_msg_xpath))

if driver.find_element_by_xpath(error_msg_xpath).text==check_msg:
    print("OK")
else:
    print("失败")
time.sleep(2)
driver.quit()