import mysql.connector
from conf import project_path
from common.read_config import ReadConfig
from common.my_log import MyLog

logger=MyLog()
class DoMysql():
    def do_mysql(self,sql,data):
        config=eval(ReadConfig(project_path.db_conf_path).getConfig('DATABASE','config'))
        cnn=mysql.connector.connect(**config)
        cursor=cnn.cursor()
        try:
            cursor.execute(sql,data)
            result=cursor.fetchone()
            return result
        except Exception as e:
            logger.error('查询出错了，报错是:%s'%e)
        finally:
            cursor.close()
            cnn.close()


if __name__ == '__main__':
    sql='select count(*) from member where mobilephone=%s'
    data=('18688773467',)#!!!元祖后要加逗号
    result=DoMysql().do_mysql(sql,data)
    print(result)