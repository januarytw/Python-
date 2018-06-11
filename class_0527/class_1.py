__author__ = 'Administrator'

def add_num(m,n):
    sum=0
    for i in range(m,n+1)
        sum+=i
    return sum

# 返回值 return + 表达式
# 1、print 会把结果直接打印到控制台，不归你管，你也拿不到这个值
# 2、return会把结果值返回给你，归你管，有你处置
# 3、返回值必须要有一个变量来进行接收
# return后面如果有代码，都会被终止。后面的代码都不会被执行


#什么时候用return
# 有你决定

#变量的作用范围
#规范：全局变量：大写字母     局部变量：小写字母

#针对函数来说，在函数外面是全局变量，在函数内部是局部变量

C=6
def add_num():
    a=8
    global C#
    C=10
    print (a+C)
print_list()
print(a)

#区别：
# A：作用域不一样
# 全局变量：在当前PY文件下，都可以调用，函数内部和外部都可以用这个值
#局部变量：只能在函数内部使用

# B：调用优先级
# 如果全局和局部的变量名重复的情况下，优先调用局部变量
#
# C：如果要修改全局变量的值：用关键字golbal
#
# D:列表和字典都可以去做更改值
LIST_1=[1,2,3]#全局变量
def print_list():
    LIST_1[2]=10#这句的意思是调用列表的方法，不是重新赋值
   # LIST_1.append(10)
    print(LIST_1)
print_list()
print (LIST_1)

###特殊情况
#如果值是列表，那么在函数里面进行赋值运算、调用函数，那么全局变量也会被更改

