__author__ = 'Administrator'

#交接作业
#把list_1车标里面的子列表的元素都一个一个输出来


#函数：内置函数
# type:len int range str list
# list:insert append extend pop sort reversed
# print input upper strip split lower
# 特点：
# 1 可以直接调用
# 2 可以重复调用

#函数 关键字def 函数名/方法名 （）：
#   代码 ，你这个函数要要实现的功能
#函数名的药酒：见名知意 小写字母 不同字母用下划线隔开

#定义函数
def print_str(name,age=18):#位置参数 默认参数
    #代码块/函数体
    print(age,"岁数"+name+"我是最棒的！") #age后面的, 可以连接数字和字符，用+号只能连接字符


#调用函数 函数名（）
print_str("张三")
print_str("李四",32)

#def 函数名（位置参数，默认参数）

# 有参数的函数
# 1函数定义的时候，需要几个位置参数，那么你调用函数的时候也要传递几个
# 2默认参数要放在位置参数后面



# def sum(a,b):
#     s=0
#     for i in range(a,b+1):
#         s+=i
#     print(s)
#
# sum(1,100)


