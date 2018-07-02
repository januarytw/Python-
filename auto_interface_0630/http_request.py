
#完成HTTP请求

import requests

class HttpRequest():
    def __init__(self,url,param):
        self.url=url
        self.param=param

    def httpRequest(self,method,cookies=None):#cookies定义了默认值
        if method.upper()=='GET':
            res=requests.get(self.url,self.param,cookies=cookies)#!!!这里要写成cookies=cookies，因为默认参数要写清参数名
        elif method.upper()=='POST':
            res=requests.post(self.url,self.param,cookies=cookies)
        else:
            print("你的请求方式不正确！")
        return res

if __name__ == '__main__':
    register="http://119.23.241.154:8080/futureloan/mvc/api/member/register"
    login="http://119.23.241.154:8080/futureloan/mvc/api/member/login"
    recharge="http://119.23.241.154:8080/futureloan/mvc/api/member/recharge"
    register_param={'mobilephone':'13541122220','pwd':'123456'}
    login_param={'mobilephone':'13541122220','pwd':'123456'}
    recharge_param={'mobilephone':'13541122220','amount':'1000'}

    #注册
    register_res=HttpRequest(register,register_param).httpRequest("get",cookies=None)
    print(register_res.json())

    #登录
    login_res=HttpRequest(login,login_param).httpRequest("get")#可以不传cookies=None，这个是默认参数
    print(login_res.json())
    cookies=login_res.cookies#cookies是登录后才产生的
    print(cookies)
    #充值
    recharge_res=HttpRequest(recharge,recharge_param).httpRequest('get',cookies=cookies)
    print(recharge_res.json())
    #充值时，是没有产生cookies的
    print(recharge_res.cookies)


