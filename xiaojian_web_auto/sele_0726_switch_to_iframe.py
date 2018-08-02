from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 打开浏览器，选择浏览器类型
driver = webdriver.Chrome()

# 最大化浏览器窗口
driver.maximize_window()

driver.get("https://ke.qq.com/")

driver.find_element_by_id("js_login").click()

WebDriverWait(driver,20,1).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="QQ登录"]')))
driver.find_element_by_xpath('//a[text()="QQ登录"]').click()

#等待iframe出现并切换,此语句直接就切换到了新的frame中
WebDriverWait(driver,20,1).until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))

#切换进入另外一个html页面
# driver.switch_to.frame("login_frame_qq")

#用户名密码登陆 - 切换之后的iframe中的html元素操作
driver.find_element_by_id('switcher_plogin').click()


# driver.find_element_by_id("u").send_keys("11111111111111")
#
# #退出iframe,回到默认的主页面
#driver.switch_to.default_content()