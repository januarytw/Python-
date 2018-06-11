__author__ = 'Administrator'

#判断 循环
'''
score=55
if score<=60:
    print ('不及格')
elif score<60：#要跟一个表达是
    print ('及格')
else：#不能跟表达式'''

# 注意：
# 冒号来控制父级 子级
# Python里面用缩进或空格来控制父级子级
# python里面代买执行顺序是 从上往下执行


#input
# aa=input("请输入一个数据")
# print (aa)

#课堂练习
#现在有一个考试系统 会根据你输入的分数判断 学生的等级
#强制规定只能输入数字
#小于0分或者大于100分 那么就是数据无效
#0~60不及格 60<=x<80及格 80<=x<90 良好 90<=x<100 优秀！
#
scores=int(input("请输入一个数字"))#字符串转换成数字类型
if scores>100 or scores<0:
    print ("无效数据")
elif scores<60:
    print ("不及格")
elif 60<=scores<80:
    print ("及格")
elif 80<=scores<90:
    print ("良好")
else:print("优秀")

#语法：
#数据类型??后面的没有记下来，会看是视频不上