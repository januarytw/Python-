__author__ = 'Administrator'
#OS 操作文件和目录
import os
'''
#获取当前文件的目录
print("1",os.getcwd())


#__file__代表当前正在编辑的文件
print("2",os.path.realpath(__file__))

#新建一个目录
os.mkdir("box")

#路径的拼接
current_dir=os.getcwd()
new_dir=os.path.join(current_dir,"dir1","dir2")#多个参数时，前面的目录必须存在
os.mkdir(new_dir)



os.path.isfile(__file__)
os.path.isdir(__file__)

print(os.path.split(os.getcwd(os.getcwdb())))#将目录和文件分开，返回时元祖类型

print(os.path.split(os.path.realpath(__file__))[0])
'''

os.path.exists("text.txt")

#列举目录下的的所有列表，返回一个列表
print(os.listdir("c:/"))
