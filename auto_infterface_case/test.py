# from openpyxl import load_workbook
# from openpyxl.styles import Font,colors,Fill,PatternFill,
#
# wb=load_workbook(r'D:\Python34\TestCode\auto_infterface_case\test_data\test_case.xlsx')
# sheet=wb['init']

a={"a":"aaa","b":4635,"c":'{"kde":"2324","w":"kfj"}'}
a1=a["c"]
print(a1)
print(type(a1))
print(type(eval(a1)))