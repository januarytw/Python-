__author__ = 'Administrator'
#file 文件操作


#r:只读  w:只写  a：追加
#非二进制文件  r r+(读写） w w+ a a+
#二进值文件 rb rb+ wb wb+ ab ab+
file=open("test.txt","r",encoding="utf-8")
file.read(5)#参数是读取的字节数，缺省是读取所有数据，从光标出开始读
file.write("哈喽")
#用w打开后，read是读不出内容的，因为w打开后文件被清空了
#先写入，再读，也读不出来，因为光标再文件的最后

#r 只读的方式打开
#r+ 读写的方式打开，写的内容会写在文件的最后面

#w 只写，如果不存在这个文件的话，就会先新建，然后根据你的要求写入内容，如果存在，那就会覆盖，重写
#w+  读写

#a 如果没有文件，会新建一个文件

file.tell()#读取光标所在位置

file.seek(0,0)#将光标移到文件头部  参数一 移动的量，参数2 相对移动几个 0 头部 1 当前文字 2 尾巴

file.close()


#上下文管理器 with open as  自动关闭文件
with open("test.txt","r") as file:
    print(file.read())