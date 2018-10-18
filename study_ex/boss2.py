import os
import xlrd
import csv

danlist = []
strpath = 'D:\\工作\\月度工作\\2018年\\2018年2月\\上载分工\\'
for x in os.listdir('D:\\工作\\月度工作\\2018年\\2018年2月\\上载分工\\'):
    print(x)
    #if os.path.isfile(x) and os.path.splitext(x)[1]=='.xlsx' or os.path.splitext(x)[1]=='.xls':
    if os.path.isfile(x):
        print('tested file %s' % strpath + x)
        wb = xlrd.open_workbook(strpath + x)
        print('open %s suc'  % x)
      

print(len(danlist))
#print(danlist)


        