__author__ = 'Administrator'
# 1：自动贩卖机： 只接受1元、5元、10元的纸币或硬币，可以1块，5元，10元。单次最多不超过10块钱。
# 饮料只有橙汁、椰汁、矿泉水、早餐奶，售价分别是3.5，4，2，4.5 写一个函数用来表示贩卖机的功能：
# 用户投钱和选择饮料，并通过判断之后，给用户吐出饮料和找零。
解：money用列表 饮料用字典
思路：先选择 后投币


money=int(input("请输入金额，只支持1元，5元，10元："))
drinks=input("橙汁、椰汁、矿泉水、早餐奶,请输入想要的饮料：")
dict_1={"橙汁":3.5,"椰汁":4,"矿泉水":2,"早餐奶":4.5,}
#判断输入的钱是否是1 5 10
if money!=1 or money!=5 or money!=10:
    print("输入的金额不对，重新输入：")
    money=input("请输入金额，只支持1元，5元，10元：")
if drinks in dict_1.keys():
    if dict_1[drinks]-money<0:
        print("您的金额不够，请继续投币：")
        money_2=input("请输入金额，只支持1元，5元，10元：")
        money=money+money_2
    elif dict_1[drinks]-money>=0:
        zhaoLing=money-dict_1[drinks]
    print("你买的饮料是：%s"%drinks)
    print("找零为：%f"%zhaoLing)




# 2：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？且统计有多少个
# def count_num(list_1):
#     result_list=[]
#     for i in list_1:
#         for j in range(1,5):
#             for k in range(1,5):
#                 if i!=j and j!=k and i!=k:
#                     new_num=i*100+j*10+k
#                     result_list.append(new_num)
#     print("最后的列表：",result_list)
#     print("符合条件的数字有：",len(result_list))