
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

    def myLog(self,msg,msg_level,log_name='auto_cases',level='DEBUG',formatStr,file_path=project_path.log_path):
        #创建日志收集器,设置级别
        logger=logging.getLogger(log_name)
        logger.setLevel(level)

        #设置输出渠道、设置输出级别
        fh=logging.FileHandler(file_path,encoding='UTF-8')
        sh=logging.StreamHandler()
        fh.setLevel(level)
        sh.setLevel(level)

        #设置输出格式
        formatter=logging.Formatter(formatStr)