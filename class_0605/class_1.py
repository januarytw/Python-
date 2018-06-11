#初始化函数 （出产就自带的） def __init__(self)
# 特点：
# 1 和普通函数一样，有关键字self
# 2 他可以单位制参数、默认参数、动态参数
# 3 他没有返回值
# 4 作用：每一个实例创建的时候 ，都会自动的带上init函数里面的参数
# 5 你自认为是这个类必须要具备的属性，请放到init函数里面



class user():
    def __init__(self,name,content):
        self.name=name
        self.content=content

    def descirber_user(self):
        print("该用户的名字 是%s"%self.name)
    def greet_user(self):
        print (self.content,self.name)

if __name__=="__main__":#python 程序入口 只有在当前模块执行的时候，才会执行
    u=user("zhang","早上好")
    u.descirber_user()
    u.greet_user()