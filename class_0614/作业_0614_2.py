# 2：结合mysqlconnector 编写一个数据库操作类，完成指定数据库的操作类。（ 请注意听老师上课的讲解题意。）

import mysql.connector

class DoMySql():
    def __init__(self,config,sql):
        self.config=config
        self.sql=sql
    def ExecuteQuery(self):
        try:
            cnn=mysql.connector.connect(**self.config)
            cursor=cnn.cursor()

            cursor.execute(self.sql)
            result=cursor.fetchall()

            cursor.close()
            cnn.close

            return result
        except Exception as e:
            print("错误：",e)

if __name__=="__main__":
    config={'host':'118.126.108.173',
        'user':'python',
        'password':'python5666',
        'port':3306 ,
        'database':'test_summer',
        }
    sql="select * from student where id=2"

    execQuery=DoMySql(config,sql).ExecuteQuery()
    print(execQuery)