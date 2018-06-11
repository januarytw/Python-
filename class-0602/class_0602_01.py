# 类与对象
#语法：class 类名：
    #包含：属性
    #函数
#规范：1 见名知意、首字母小写、驼峰命名

#举例：创建一个对象/实例化
#创造实例：a=类名（）  那么a就是一个对象

# 写一个那朋友类

class boyFriend():
    sex="boy"
    age="20"
    money=10000
    def code(self):
        return ("沉迷代码，无法自拔")
    def cooking(self):
        return ("会做饭")

#实例化
boy_friend=boyFriend()
print(boy_friend.sex)
print(boy_friend.age)
print(boy_friend.code())
print(boy_friend.cooking())

#类与对象的一些特征和操作注意点
# 1 类里面的属性和函数只能是类的实例去调用，不能直接调用
# 2 调用属性的方法：实例名.属性名
# 3 调用函数的方法：实例名.函数名