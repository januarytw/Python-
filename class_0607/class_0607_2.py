# requests模块
# 安装：cmd  pip install requests

import requests
#
# #get请求
# url=
# requests.get(url).text  #返回的是字符串str
# requests.get(url).json  #返回的是字符串dict  !!!比较常用
# requests.get()
#
# #post请求
# request.post(url)


#写一个HTTP请求类 里面有2个参数，分别完成GET和POST请求

class HttpRequest():
    def __init__(self,url,param=None):#空用None
        self.url=url
        self.param=param
    # def get(self,url,param):
    #     response=requests.get(self.url,self.param)
    #     return response.json()
    #
    # def post(self,url,param):
    #     response=requests.post(self.url,self.param)
    #     return response.json()
    #可以用以下的代码优化

    def get_post_request(self,method):
        try:
            if method.upper()=="GET":
                response=requests.get(self.url,self.param)
                return response.json()
            elif method.upper()=="POST":
                response=requests.post(self.url,self.param)
                return response.json()
        except Exception as e:
            print ("请求失败，出现的错误是%s"%e)#错误抓起来，然后代码可以继续运行，把异常信息获取到，并对异常进行处理
            raise e#你处理完了以后，要把错误物归原主。错误还是会报出来，程序终止
if __name__=="__main__":
    url=''
    data=''
