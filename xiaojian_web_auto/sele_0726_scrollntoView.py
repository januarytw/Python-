from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.baidu.com")

# 隐形等待
driver.implicitly_wait(30)

driver.find_element_by_id("kw").send_keys("selenium webdriver")
driver.find_element_by_id("su").click()

WebDriverWait(driver,20,1).until(EC.presence_of_element_located((By.XPATH,'//span[text()="4" and @class="pc"]')))

#1找到元素
element=driver.find_element_by_xpath('//span[text()="4" and @class="pc"]')

#2/执行js语句。需要传入定位
driver.execute_script("arguments[0].scrollIntoView();",element)

#3、操作元素
element.click()