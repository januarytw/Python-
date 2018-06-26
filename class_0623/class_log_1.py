#日志

#引入模块
import logging

# logging.debug("siliy是傻瓜")
# logging.info("info信息")
# logging.warning("warning信息")
# logging.error("error信息")
# logging.critical("critical信息")


#创建一个日志收集器
logger=logging.Logger("huahua","DEBUG")#Logger大写  定级别是用大写

#创建输出渠道
#输出到控制台
ch=logging.StreamHandler()
ch.setLevel('INFO')
formatter=logging.Formatter('%(asctime)s-[%(levelname)s]-%(filename)s-%(name)s-日志信息:%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

#输出到文件
fh=logging.FileHandler('test_log.txt',encoding='UTF-8')#!!有中文是要设置编码
fh.setLevel("INFO")
formatter=logging.Formatter('%(asctime)s-[%(levelname)s]-%(filename)s-%(name)s-日志信息:%(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


if __name__ == '__main__':
    logger.debug("siliy是傻瓜")
    logger.info("info信息")
    logger.warning("warning信息")
    logger.error("error信息")
    logger.critical("critical信息")





