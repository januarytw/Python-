
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
import time

# 打开浏览器，选择浏览器类型
driver = webdriver.Chrome()

# 最大化浏览器窗口
driver.maximize_window()

#访问页面
driver.get("http://www.baidu.com")

setting_locator='//*[@id="u1"]//*[@name="tj_settingicon"]'

#先找到这个元素
seeting_ele=driver.find_element_by_xpath(setting_locator)

#实例化Actionchains,再调用方法，最后再调用perform来执行
ActionChains(driver).move_to_element(seeting_ele ).perform()


#悬浮下拉框的操作，点击高级搜索
advanced_search_locator = '//a[text()="高级搜索"]'

#先等待
WebDriverWait(driver,20,1).until(EC.visibility_of_element_located((By.XPATH,advanced_search_locator)))

#再操作
driver.find_element_by_xpath(advanced_search_locator).click()

#下拉框的操作
from selenium.webdriver.support.ui import Select

select_loactor = '//select[@name="ft"]'
WebDriverWait(driver,20,1).until(EC.visibility_of_element_located((By.XPATH,select_loactor)))

#找到Select元素
ele_select  =driver.find_element_by_xpath(select_loactor)

#实例化Select类 - 参数为select元素对象
s = Select(ele_select)
#下标 - 选择元素
s.select_by_index(2)
time.sleep(5)
#value值
s.select_by_value("rtf")
time.sleep(5)
#text
s.select_by_visible_text("微软 Powerpoint (.ppt)")