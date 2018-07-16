import os
from common.read_config import ReadConfig


print(os.path.split(os.path.realpath(__file__)))

project_conf_path=os.path.split(os.path.realpath(__file__))[0]+'\project.conf'
# print(project_conf_path)

project_path=ReadConfig(project_conf_path).getConfig('PROJECT_PATH','project_path')
# print(project_path)


#以下为系统中用到的路径

#测试数据的路径
test_data_path=os.path.join(project_path,'test_data','test_case.xlsx')
#print(test_data_path)


#日志输出路径
log_path=os.path.join(project_path,'test_result','log','test_log.txt')

#测试报告路径
report_path=os.path.join(project_path,'test_result','http_report','html_report')

#用例配置文件的路径
case_conf_path=os.path.join(project_path,'conf','case.conf')

#http配置文件的路径
config_conf_path=os.path.join(project_path,'conf','http.conf')

#数据库配置文件路径
db_conf_path=os.path.join(project_path,'conf','db.conf')

