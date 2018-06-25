'''
配置文件
以.conf结尾
包含标签和配置项
标签用[]
read方法中如果有中文，参数encoding=udf-8

[HTTP]#此项叫section
ip:http://192.168.1.1
#ip叫option，后面的值叫value

从配置文件中读出来的值时str类型
如果要字典类型

'''
import configparser

cf=configparser.ConfigParser()
cf.read("db.conf")
config=cf.get('DATABASE','config')
print(eval(config))