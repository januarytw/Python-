
# 1.txt中存了很多数据，一行为一个请求数据，怎么样才能把这些数据读取到并且存到list中。数据的存储格式见txt附件
# 请把数据从TXT里面读取出来，然后存储为这种数据格式：
# [{'url':'http://119.23.241.154:8080/futureloan/mvc/api/member/login','mobilephone':'13760246701','pwd':'123456'} ,
#  {'url':'http://119.23.241.154:8080/futureloan/mvc/api/member/login','mobilephone':'15678934551','pwd':'234555'}]
#[{'pwd': '123456', 'mobilephone': '13760246701', 'url': 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'},
# {'pwd': '234555', 'mobilephone': '15678934551', 'url': 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'}]

# file=open("test_1.txt","r")
# a=file.read()
# print(a)
'''
with open("test_1.txt") as f:
    #print(f.read())
    lines=list(f)
    # print(lines)
    newLines=[]
    a=[]
    for i in lines:
        newLines.append(i.split(","))
    print(newLines)

    for j in newLines:
        print(j)
        for k in j:
            # print(k)
            a.append(k.split(":",1))
            # print(a)
    print(a)
    print(dict(a))
'''#这种方法最后在转换成dict时会因为key值有重复，会将之前的值覆盖。


with open("test_1.txt") as f:
    a=[]#存放每一行的数据，去除回车，并用,把每组值分开，形成新的列表
    b=[]#存放每组数据用：分开后的值
    c=[]#存放最终的结果
    for line in f.readlines():
        a=line.strip("\n").split(",")
        print("a:",a)
        for i in a:
            b.append(i.split(":",1))#url中有多个：，所以只能分割一次,将一组数据分割后，存入b列表中
        print("b:",dict(b))#之后要将整个一组数据转换成一个字典
        c.append(dict(b))#将这个字典格式的数据添加C列表中
    # print("c",c)
    with open("test_1_convert.txt","w+") as file:
        # print(type(c))
        file.write(str(c))#要以字符串的格式写入