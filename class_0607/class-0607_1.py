# 超继承：比较贪心的继承，你的也是我的，我的还是我的
# 其实就是调用父类的方法

class add_1():
    def add(self,a,b):
        print("两数之和：",a+b)

class add_2(add_1):
    #要求：计算ab两数之和，然后再计算abc三数之和
    def add(self,a,b,c):
        super(add_2,self).add(a,b)#这里是调用父类的add的方法
        #其实，把父类的方法复制过来也是可以的，但如果父类的方法代码多的时候就不适合了，所以用super
        # print("两数之和：",a+b)
        print("三数之和是",a+b+c)

t=add_2()
t.add(1,2,3)

