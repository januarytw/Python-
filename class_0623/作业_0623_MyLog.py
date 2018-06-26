# 0623作业
# 1：输出格式formatter可配置
# 2:输出到控制台还是文件：可配置
# 3：输出级别可配置
# 4：输出的文件地址：可配置

#引入模块
import logging
from class_0621.作业_0621_ReadConfig import ReadConfig

class MyLog:

    def myLog(self,name,state,level,formatStr,out_file_path):
        #创建一个日志收集器
        logger=logging.Logger(name,level)#Logger大写  定级别是用大写
        if state=='1':
            #创建输出渠道,输出到控制台
            ch=logging.StreamHandler()
            ch.setLevel(level)
            formatter=logging.Formatter(formatStr)
            ch.setFormatter(formatter)
            logger.addHandler(ch)
        elif state=='2':
            #输出到文件
            fh=logging.FileHandler(out_file_path,encoding='UTF-8')#!!有中文是要设置编码
            fh.setLevel(level)
            formatter=logging.Formatter(formatStr)
            fh.setFormatter(formatter)
            logger.addHandler(fh)
        elif state=='3':
            #创建输出渠道,输出到控制台
            ch=logging.StreamHandler()
            ch.setLevel(level)
            formatter=logging.Formatter(formatStr)
            ch.setFormatter(formatter)
            logger.addHandler(ch)
            #输出到文件
            fh=logging.FileHandler(out_file_path,encoding='UTF-8')#!!有中文是要设置编码
            fh.setLevel(level)
            formatter=logging.Formatter(formatStr)
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        return logger


if __name__ == '__main__':
    readConfig=ReadConfig('log.conf')
    name="andy"
    state=readConfig.getConfig('CONFIG','state')
    level=readConfig.getConfig('CONFIG','level')
    formatStr=readConfig.getConfig('CONFIG','formatter')
    out_file_path=readConfig.getConfig('CONFIG','out_file_path')

    logger=MyLog().myLog(name,state,level,formatStr,out_file_path)
    logger.debug("siliy是傻瓜")
    logger.info("info信息")
    logger.warning("warning信息")
    logger.error("error信息")
    logger.critical("critical信息")
