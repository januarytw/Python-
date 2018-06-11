__author__ = 'Administrator'

#for 循环   遍历元素 每个元素都会读一遍
#in 后跟一个数据范围 列表 字符串 元组 数据范围(1,2,3,4,5,6)
#遍历元素的顺序  从左到右


# str_1="hello python"
# for i in str_1:
#     print (i)

# list_1=[1,2,3,4,44]
# for i in list_1:
#     print (i)
#

# tuple_1=(1,2,3,4,54,56)
# for i in tuple_1:
#     print (i)


# dict_1={"age":18,"sex":"girl"}
# for value in dict_1.values():
#     print (value)


#range函数：会根据你指定的返回生成一个整数序列
result=list(range(5))#b吧整数序列转成列表
result1=list(range(8,0,-2))
print (result1)

#range(n) 生成的是0到n-1的整数序列
#ragne(m,n) 生成的是m到n-1的整数序列
#ragne(m,n,k) 生成的是m到n-1的整数序列，每个数据之间相隔k 等差数列
