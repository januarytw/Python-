#讲解上次课的数据库操作类,此方法为老师写的方法
import mysql.connector

class DbInfo:
    def __init__(self,config):
        self.config=config

    def get_cnn(self):
        return mysql.connector.connect(**self.config)

    def get_data(self,query,condition,state):
        cnn=self.get_cnn()
        cursor=cnn.cursor()
        if state==1:#select
            cursor.execute(query,condition)
            result=cursor.fetchall()
        elif state==2:#执行插入，修改，删除操作
            cursor.execute(query,condition)
            cursor.execute("commit")
            result=[]
        cursor.close()
        cnn.close()
        return result

if __name__ == '__main__':

    config={'host':'118.126.108.173',
            'user':'python',
            'password':'python5666',
            'port':3306 ,
            'database':'test_summer',
            }
    query_1="select * from student where id<%s"
    confition_1=(20,)

    print(DbInfo(config).get_data(query_1,confition_1,1))
