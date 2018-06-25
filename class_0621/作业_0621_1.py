# 1.作业：请写一个类 专门负责配置信息的读写

import configparser

class ReadConfig:
    def __init__(self,file):
        self.file=file

    def getConfig(self,section,option):
        cf=configparser.ConfigParser()
        cf.read(self.file)
        config=cf.get(section,option)
        return config

rc=ReadConfig("db.conf").getConfig("DATABASE","config")
print (rc)

# 2.写一个邮件类：请你把DDT测试用例执行完毕之后的HTML报告作为附件发给华华的邮箱： 204893985@qq.com