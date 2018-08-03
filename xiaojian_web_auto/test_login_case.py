from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()
driver.maximize_window()

#打开网址
driver.get("http://120.79.176.157:8012/Index/login.html")

#登录
driver.find_element_by_xpath('//input[@name="phone"]').send_keys("18684750553")
driver.find_element_by_xpath('//input[@name="password"]').send_keys("python")
driver.find_element_by_tag_name("button").click()

# 验证
try:
