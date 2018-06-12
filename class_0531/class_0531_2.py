__author__ = 'Administrator'
#异常处理：针对异常发生的时候，进行的一些处理动作
#语法：
# 第一种异常
# try:#监控你觉得可能会有问题的代码，或可能会出现的违规操作的代码
#     pass
# except:#针对try监控的代码出现的代码的处理
#     pass
#
#
# 第二种异常
# try:#监控你觉得可能会有问题的代码，或可能会出现的违规操作的代码
#     pass
# except:#针对try监控的代码出现的代码的处理
#     pass
# finally:#不管有无异常，都要进行finally下面的代码。！！比如：打开一个文件，出现异常了，但还是要关闭的，所以要在finally中关闭
#     pass
#
# 第三种异常
# try:#监控你觉得可能会有问题的代码，或可能会出现的违规操作的代码
#     pass
# except:#针对try监控的代码出现的代码的处理
#     pass
# else:#异常发生，不执行else下面的代码；异常不发生，就行else下的代码
#     pass
#
# 第四种异常
# try:
#     pass
# finally:
#     pass


try:
    print(a)
except NameError as e:#处理指定类型的错误   Exception是所以异常的基类，处理所有的异常
    print("错误是：",e)
finally:
    print("我还是要执行的")

