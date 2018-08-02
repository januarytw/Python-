
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("D:\\课件目录\\web自动化-selenium\\test-3.html")

#1、某一个操作导致了alert弹框的出现
driver.find_element_by_id("pres").click()

#2、等待这个框出现
WebDriverWait(driver,10,1).until(EC.alert_is_present())

#3、切换到这个框
alert = driver.switch_to.alert

#4、 关闭这个框
print(alert.text)
alert.accept()