
from selenium import webdriver


driver = webdriver.Chrome()

driver.maximize_window()

driver.set_window_size()

# 关闭浏览器窗口(关闭当前窗口）
driver.close()

# 关闭浏览器（并结束浏览器驱动的进程）
driver.quit()

#访问页面
driver.get("http://www.baidu.com")

# 隐形等待
driver.implicitly_wait(30)

driver.find_element_by_id("kw").sen
driver.find_element_by_id("su").click()

#！！！当页面发生变化的时候，一定要加等待
#等待
# 1、sleep-强制等待
# 2、智能等待-设置等待的上限，在这个上限范围之内，任何时候等到了就可以继续往下操作了
# （1）隐式等待，从开始会话到结束，只需设置一次。全局通用。只要是find_element,就会等待它的出现
#     driver.implicitly_wait(30)
# （2）显性等待