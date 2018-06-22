# 1：利用6-12号写的excel数据读取类以及6月9号写的HTTP单元测试类，完成老黄历的单元测试，且输出测试报告。
# （注意是要从Excel里面获取测试 数据哦~并且把测试结果写回到Excel中去。请注意听老师上课的讲解题意。）


'''一、HTTP请求类 里面有2个参数，分别完成GET和POST请求'''
import requests
class HttpRequest():
    def __init__(self,url,data=None):#空用None
        self.url=url
        self.data=data

    def get_post_request(self,method):
        try:
            if method.upper()=="GET":
                response=requests.get(self.url,self.data)
                return response.json()
            elif method.upper()=="POST":
                response=requests.post(self.url,self.data)
                return response.json()
        except Exception as e:
            print ("请求失败，出现的错误是%s"%e)
            raise e



'''二、操作excel'''
from openpyxl import load_workbook
class DoExcel():
    def __init__(self,file_path,sheet_name):
        self.file_path=file_path
        self.sheet_name=sheet_name

    #读取Excel数据
    def readData(self):#此处可以改进一下，利用初始化函数
        try:
            work_book=load_workbook(self.file_path)
            sheet=work_book[self.sheet_name]
            i=1
            list_1=[]
            list_2=[]
            while i<sheet.max_row:#!!!!此处可以用for in range()
                j=1
                while j<=sheet.max_column:
                    list_1.append(sheet.cell(i+1,j).value)
                    j+=1
                i+=1
                list_2.append(list_1)
                list_1=[]
            return list_2
        except Exception as e:
            print("读取出错了：",e)

    #写入测试结果
    def writeData(self,r,c,msg):
        try:
            work_book=load_workbook(self.file_path)
            sheet=work_book[self.sheet_name]
            sheet.cell(r,c).value=msg
            work_book.save(self.file_path)#保存
        except Exception as e:
            print("写入出错了：",e)



'''三、http请求类的单元测试'''
import requests
import unittest
from ddt import ddt,data,unpack

class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        self.doExcel=DoExcel("case.xlsx","test_data")
        print("测试开始！")

    def test_get_post_request(self):
        excelResult=self.doExcel.readData()
        # print("读取的结果",excelResult)
        first_row=2
        for list_sub in excelResult:
            h=HttpRequest(url=list_sub[3],data=list_sub[4])
            response=h.get_post_request(list_sub[2])

            print(list_sub)
            print("canshu",list_sub[3],list_sub[4],list_sub[2])
            print(response)
            try:
                self.assertEqual("Success",response["reason"])#正常就通过，结果为否时，抛出异常
                result='pass'
            except AssertionError as e:
                print("出错了",e)
                result='file'
                raise e
            finally:
                self.doExcel.writeData(first_row,7,response)
                self.doExcel.writeData(first_row,8,result)
            first_row+=1


    def tearDown(self):
        print("测试结束！\n")

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(TestHttpRequest("test_get_post_request"))
    runner=unittest.TextTestRunner()
    runner.run(suite)
