
import logging
from conf import project_path

class MyLog:

    '''def myLog(self,name,state,level,formatStr,out_file_path):
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

        return logger'''

    def myLog(self,msg,msg_level,log_name='auto_cases',level='DEBUG',file_path=project_path.log_path):
        #创建日志收集器,设置级别
        logger=logging.getLogger(log_name)
        logger.setLevel(level)

        #设置输出渠道、设置输出级别
        fh=logging.FileHandler(file_path,encoding='UTF-8')
        sh=logging.StreamHandler()
        fh.setLevel(level)
        sh.setLevel(level)

        #设置输出格式
        formatter=logging.Formatter('[%(levelname)s]%(asctime)s[日志信息]:%(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        logger.addHandler(sh)
        logger.addHandler(fh)
        if msg_level=='DEBUG':
            logger.debug(msg)
        elif msg_level=='INFO':
            logger.info(msg)
        elif msg_level=='WARNING':
            logger.warning(msg)
        elif msg_level=='ERROR':
            logger.error(msg)
        elif msg_level=='CRITICAL':
            logger.critical(msg)
        #使用完成后要记得移除handler
        logger.removeHandler(fh)
        logger.removeHandler(sh)

    def debug(self,msg):
        self.myLog(msg,'DEBUG')

    def info(self,msg):
        self.myLog(msg,'INFO')

    def warning(self,msg):
        self.myLog(msg,'WARNING')

    def error(self,msg):
        self.myLog(msg,'ERROR')

    def critical(self,msg):
        self.myLog(msg,'CRITICAL')


if __name__ == '__main__':
    MyLog().info('hello')