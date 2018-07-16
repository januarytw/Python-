#操作数据库
#连接数据库 需要输入什么信息：IP地址、端口、用户名、密码

import mysql.connector

config={'host':'118.126.108.173',
        'user':'python',
        'password':'python5666',
        'port':3306 ,
        'database':'test_summer',
        }

#登录数据库
cnn=mysql.connector.connect(**config)

#游标--cursor--获取操作数据库的权限
cursor=cnn.cursor()



#增删改查
sql="select * from student where id=%s and age>%s"
#传参：元祖
data=(2,20)#!!!!元祖是一个值时，要用一个逗号

#执行语句
cursor.execute(sql,data)
# 插入
sql_insert='insert into student(age,name) values(%s,%s)'
sql_insert='insert into student(age,name) values(%(age)s,%(name)s)'
data=(18,"silly")
data=[(18,'zhang'),(28,'ange')]#列表
data={}
cursor.execute(sql_insert,data)
cursor.executemany(sql_insert,data)
cursor.execute('commit')#插入操作后，要提交


result_1=cursor.fetchone()#读取一条数据 返回的是元祖
result_2=cursor.fetchall()#读取全部数据  返回的是列表，列表中有元祖

#读取查询结果 fetchone  fetchall 如果结果是一条，用两个都可以。
# 如果结果有多条数据，用fetchone,会报错（mysql.connector.errors.InternalError: Unread result found 意思是还有数据没有被读出）
#!!!!cursor就像光标一样，读取一条后，游标会停留在第二行，

print(result_1)
# print(result_2)


#关闭cursor
cursor.close()
cnn.close

#关闭cnn
