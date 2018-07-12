'''
操作excel，读取和写入操作
'''

from openpyxl import load_workbook
# from openpyxl.styles import Font,colors
from conf import project_path
from common.read_config import ReadConfig

class DoExcel():
    def __init__(self,file_path,sheet_name):
        self.file_path=file_path
        self.sheet_name=sheet_name

    #读取为注册的手机号
    def no_reg_tel(self):
        wb=load_workbook(self.file_path)
        sheet=wb['init']
        no_reg_tel=sheet.cell(1,2).value
        return no_reg_tel

    #更新未注册的手机号，手机号码+1
    def update_tel(self,new_tel):
        wb=load_workbook(self.file_path)
        sheet=wb['init']
        sheet.cell(1,2).value=new_tel
        wb.save(self.file_path)

    #读取excel中的用例
    def read_data1(self,mode,case_list):#mode：读取用例模式，0为指定用例，1为全部用例。case_list：用例列表
        #载入文件
        wb=load_workbook(self.file_path)
        #指定工作表
        sheet=wb[self.sheet_name]
        #实现每一行数据存在一个列表里面，然后所有行的数据存在一个大列表里面
        test_data=[]#存储所有行的数据
        no_reg_tel=self.no_reg_tel()
        if mode=='1':
            for i in range(2,sheet.max_row+1):#从excel的第2行开始读；range取左不取右，所以要+1
                sub_data=[]#存储每一行的数据
                for j in range(1,8):
                    if j==6:
                        param=eval(sheet.cell(i,6).value)
                        if param['mobilephone']=='first_tel':
                            param['mobilephone']=no_reg_tel
                            sub_data.append(param)
                    else:
                        sub_data.append(sheet.cell(i,j).value)
                test_data.append(sub_data)
        elif mode=='0':
            for i in case_list:
                sub_data=[]#存储每一行的数据
                for j in range(1,8):
                    if j==6:
                        param=eval(sheet.cell(i+1,6).value)
                        if param["mobilephone"]=='first_tel':
                            param['mobilephone']=no_reg_tel
                            sub_data.append(param)
                    else:
                        sub_data.append(sheet.cell(i+1,j).value)
                test_data.append(sub_data)
        self.update_tel(str(int(no_reg_tel)+1))

        return test_data

    def read_data(self,mode,case_list):
        no_reg_tel=self.no_reg_tel()
        wb=load_workbook(self.file_path)
        sheet=wb[self.sheet_name]
        test_data=[]#存储所有行的数据
        if mode=='1':#执行所有用例
            for i in range(2,sheet.max_row+1):
                sub_data=[]#存储每一行的数据
                for j in range(1,8):
                    if j==6:
                        param=eval(sheet.cell(i,6).value)
                        if param['mobilephone']=='first_tel':
                            param['mobilephone']=no_reg_tel
                            sub_data.append(param)
                    else:
                        sub_data.append(sheet.cell(i,j).value)
                test_data.append(sub_data)
        elif mode=='0':
            for i in case_list:#！！！此处需要case_list是list类型的，从配置文件里读取出来要进行转换
                sub_data=[]#存储每一行的数据
                for j in range(1,8):
                    if j==6:
                        param=eval(sheet.cell(i+1,6).value)#i+1的意思 ：是从第二行开始的
                        if param['mobilephone']=='first_tel':
                            param['mobilephone']=no_reg_tel
                        sub_data.append(param)#如果有first_tel这个就替换后加到列表中，如果没有就直接加入

                    else:
                        sub_data.append(sheet.cell(i+1,j).value)
                test_data.append(sub_data)
        self.update_tel(str(int(no_reg_tel)+1))
        return test_data

    #写入excel
    def write_data(self,row,actual,result):
        #载入文件
        wb=load_workbook(self.file_path)
        #指定工作表
        sheet=wb[self.sheet_name]
        #写入测试数据时，固定写入第8和9列
        sheet.cell(row,8).value=actual
        sheet.cell(row,9).value=result
        # sheet.cell.front=front(colors=color.RED)
        #保存
        wb.save(self.file_path)


if __name__ == '__main__':
    mode=ReadConfig(project_path.case_conf_path).getConfig('CASE','mode')
    case_list=eval(ReadConfig(project_path.case_conf_path).getConfig('CASE','case_list'))
    print (type(case_list))
    testdata=DoExcel(project_path.test_data_path,"test_data").read_data(mode,case_list)
    print(testdata)

