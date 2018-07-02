import configparser

class ReadConfig:
    def __init__(self,file_path):
        self.file_path=file_path

    def getConfig(self,section,option):
        cf=configparser.ConfigParser()
        cf.read(self.file_path,encoding='UTF-8')
        value=cf.get(section,option)
        return value

if __name__ == '__main__':
    # import os
    # path=os.path.abspath("..")
    # print(path)
    rc=ReadConfig("../conf/config.conf").getConfig("HTTP","ip")
    print (rc)