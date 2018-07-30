#引入库 selenium webdriver
from selenium import webdriver


#选择Google浏览器
driver = webdriver.Chrome()
#参数如下
# __init__(self, executable_path="chromedriver", port=0,
#                  options=None, service_args=None,
#                  desired_capabilities=None, service_log_path=None,
#                  chrome_options=None):
#service指的就是浏览器deriver

driver.get("http://www.baidu.com")

# web页面元素定位，分为8种

#1、通过ID来定位，确定id是不会比变的，有些项目的元素id是会变的
# driver.find_element_by_id("kw")   返回的是WebElement实例化对象，可以直接调用类的方法
driver.find_element_by_id("kw")

#2、通过name来定位  name并不是唯一的  有可能有多个元素
driver.find_element_by_name("wd")  #只会找到一个元素
driver.find_elements_by_name("wd")  #找到所有的元素，并存在列表中返回

#3、通过标签名定位  不是唯一的，也会找到多个
driver.find_element_by_tag_name("input")

#4、通过class属性来定位  不是唯一的
driver.find_element_by_class_name("s_ipt")

#5、通过链接的文本内容来定位
driver.find_element_by_link_text("学术")

#6、通过链接；通过部分匹配链接的文本内容来定位
driver.find_element_by_partial_link_text("产品")

# 7、通过xpath定位 --标签名+属性
#绝对定位 /html/body/div[2]/div/form/div[2]/input
#

#相对定位 //*[@id="kw"]   不考虑位置关系，不考虑层级定位
#1、有没有这个元素（标签名）2、如果有，如何唯一找到它
#规范：//标签名[@name=""]
#//*[@id="u1"]/a[6]
#尽量不要使用下标
#当元素的本身属性并不能唯一定位，可以先定位其祖先或其后辈（唯一定位），然后在来定位它（缩小定位范围
#相对定位可以组合绝对定位来用
#and来连接多个表达式//a[@name='' and @class='']



