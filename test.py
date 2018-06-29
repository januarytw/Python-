import requests

url='http://119.23.241.154:8080/futureloan/mvc/api/member/login'
data={'mobilephone':'13141222222','pwd':'123456'}
s=requests.session()
s.get(url,data)