import os
from common.read_config import ReadConfig

project_conf_path=os.path.split(os.path.realpath(__file__))[0]+'\project.conf'
print(project_conf_path)