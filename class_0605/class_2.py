# 继承：全部继承、部分继承、多继承、超继承
# import 和 from import
# import class_0605.class_1#具体到模块名
# from class_0605.class_1 import user#具体到类名

class a(b): #完全继承

部分继承：重写父类的函数
当子类和父类有重名的方法时，就叫重写。子类的实例调用的函数是自己的函数


class c(a,b):#多继承

超继承：
def ab()
    super(子类,self).父类的函数