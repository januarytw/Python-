# 函数参数：
# 默认参数：
def add(a=1,b=2,c=3):
print(a+b+c)

#指定默认参数
add(b=10)  

# 动态参数---可以传递任意个参数，参数前加一个*

def add_2(*args):
    sum=0
    for item in args:
        sum+=sum+item
    print(sum)
#传进来的参数会当做元祖处理
add_2(1,2,3,4)

# 两个**，传进来会当做字典处理
def add_3(**args):
    print()
add_3(x=1,y=2)

#-----------------
# import用法
# 导入函数时：import 包名.模块名
import class_0527.class_1  #不能到函数名

# 调用函数：包名.模块名.函数名（参数）
class_0527.class_1.add_num()

# 另种导入方法：from 包名.模块名 import 函数名---推荐使用
from class_0527.class_1 import add_num #可以到函数名
# 调用：函数名（参数）

#！！！lib目录下，可以直接去引用
