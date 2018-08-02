#显性等待

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import webdriver

# 打开浏览器，选择浏览器类型
driver = webdriver.Chrome()

# 最大化浏览器窗口
driver.maximize_window()

#访问页面
driver.get("http://www.baidu.com")

#点击登陆按钮
driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()

#表达式 - 登录弹出框 - 用户名密码登陆方式
login_by_user_id = "TANGRAM__PSP_10__footerULoginBtn"

#显性等待 - 明确的条件
locator = (By.ID,login_by_user_id)
WebDriverWait(driver,15,1).until(EC.visibility_of_element_located((By.ID,login_by_user_id)))

#操作 -
driver.find_element_by_id(login_by_user_id).click()
