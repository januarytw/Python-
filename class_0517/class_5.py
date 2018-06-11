
# 作业：
# 1:把a 和b的值一起组合打印出来 a=[1,2,3,"this is a list"] b=[4,5,6,"这是第二个列表"]
# 2：输出列表a两次
# 3：取a列表第一个值
# 4：取a列表第二个和第三个值
# 5：取a列表第三个值以及到末尾的所有值
# 6：L = [ ['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa'] ] 打印Apple、Python、Lisa
# 7.合并下面的两个list并去重（去重可以使用set函数） list1 = [2, 3, 8, 4, 9, 5, 6] list2 = [5, 6, 10, 17, 11, 2]
# 8：a=5,b=9,如何交换着两个值
# 9:s="lemon ptyhon",如何打印这个字符串两次

#解题：
# 1:把a 和b的值一起组合打印出来
a=[1,2,3,"this is a list"]
b=[4,5,6,"这是第二个列表"]
print (a+b)

# 2：输出列表a两次
print (a*2)

# 3：取a列表第一个值
print (a[0])

# 4：取a列表第二个和第三个值
print (a[1:3])

# 5：取a列表第三个值以及到末尾的所有值
print (a[2:])

# 6：L = [ ['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa'] ] 打印Apple、Python、Lisa
L = [ ['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa'] ]
print (L[0][0],L[1][1],L[2][2])

# 7.合并下面的两个list并去重（去重可以使用set函数）
list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]
list1.extend(list2)
print (set(list1+list2))
##疑问：为什么结果的list是{}呢？

# 8：a=5,b=9,如何交换着两个值
a=5
b=9
c=a
a=b
b=c
print('a=%s'%a)
print('b=%s'%b)

# 9:s="lemon ptyhon",如何打印这个字符串两次
s="lemon ptyhon"
print (s*2)