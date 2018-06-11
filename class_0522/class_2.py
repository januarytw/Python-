__author__ = 'Administrator'
#循环  while  for

a=1
while True:#while 也是跟条件表达式  布尔值  !!如果用True 注意大小写
    a+=1
    print (a)
    if a<100:
        continue #继续当前循环
    elif a>100:
        break #跳出循环