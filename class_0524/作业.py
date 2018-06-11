# 05-24 作业
# 1、一个足球队在寻找年龄在i岁到j岁 （i>j） 的性别为sex (sex 从f、m里面选择）的人加入。
# 编写一个函数，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。实现这个函数的功能，并且调用函数。
# def football(sex_d,min,max,k):
#     total=0
#     for i in range(k):
#         age=int(input("请输入年龄："))
#         sex=input("请输入性别（m代表男性，f代表女性：")
#         if min<=age<=max and sex==sex_d:
#             print("你可以加入足球队")
#             total+=1
#         else:
#             print("很抱歉，你的条件不符合！")
#     print("\n满足条件的总人数：%d"%total)
#
# football("m",10,20,2)

# 2：对任意字符串，编写一个函数，实现转换成一个列表，每个字符对应列表里面的一个元素。
# def str_to_list(str_1):
#     list_1=[]
#     for item in str_1:
#         list_1.append(item)
#     print(list_1)
#
# str_to_list("hello")


# 3：定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典。
def str_include_dict(d,s):
    if d not in s.values():
        t=input("字典键值不存在，输入键值：")
        s[t]="d"
        print (s)
    else:
        print("字符串包含在字典中")


str_include_dict("3",{"a":'4',"b":"5"})