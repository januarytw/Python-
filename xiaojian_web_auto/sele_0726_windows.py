from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.baidu.com")

driver.implicitly_wait(30)

driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()

tieba_locator = '//a[contains(text(),"吧_百度贴吧")]'
WebDriverWait(driver,20,1).until(EC.presence_of_element_located((By.XPATH,tieba_locator)))

#1、找到该元素
#EC.new_window_is_opened
handles =   driver.window_handles
print(handles)

#点击贴吧，弹出新的窗口
driver.find_element_by_xpath(tieba_locator).click()

#等待新窗口出现 - 根据窗口数量 的变化 来判断
WebDriverWait(driver,20,1).until(EC.new_window_is_opened(handles))

#重新获取一下handles
handles =   driver.window_handles
print(handles)

#切换进新的窗口
driver.switch_to.window(handles[-1])
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")