import os
import xlrd
import csv
import json
import re
import set

danlist = []
strpath = 'D:\\工作\\月度工作\\2018年\\2018年2月\\上载分工\\'
for x in os.listdir('D:\\工作\\月度工作\\2018年\\2018年2月\\上载分工\\'):
    #print(x)
    #if os.path.isfile(x) and os.path.splitext(x)[1]=='.xlsx' or os.path.splitext(x)[1]=='.xls':
    if  1 > 0 :
        #print('tested file %s' % strpath + x)
        wb = xlrd.open_workbook(strpath + x)
        #print('open %s suc'  % x)
        for name in wb.sheet_names():
            #print('sheet %s' % name)
            s=wb.sheet_by_name(name)
            #print('row : %s' % s.nrows)
            #print('col : %s' % s.ncols)
            if s.nrows > 0:
                #print(s.row(0))
                #print (s.row_values(0))
                cellvalue = s.row_values(0)
                try:
                    chargename = -1
                    danid = -1
                    danname = -1
                    danver = -1
                    #print(cellvalue)
                    for index in range(len(cellvalue)):
                    
                        #print(cellvalue[index])
                        if '深圳负责人' in str(cellvalue[index]):
                            chargename = index
                            
                        if '单号' in str(cellvalue[index]):
                            danid = index
                            
                        if '需求名称' in str(cellvalue[index]):
                            danname = index
                           
                        if '版本' in str(cellvalue[index]):
                            danver = index
                            
                    #chargename = cellvalue.index('深圳负责人')
                    #danid = cellvalue.index('单号')
                    #danname = cellvalue.index('需求名称') 
                    #danver = cellvalue.index('版本号')
                                         
                    if chargename >=0 and danid >=0 and danname >=0 :
                        for i in range(s.nrows-1):
                            cell = s.row_values(i+1)
                            if re.match(r'BR\d{12}',cell[danid]):
                                if danver >=0:
                                    ver = cell[danver]
                                else:
                                    ver = ''
                                danlist.append([str(cell[danid]).strip().replace('\n',''),str(cell[danname]).strip().replace('\n',''),str(ver).strip().replace('\n',''),str(cell[chargename]).strip().replace('\n',''),x])
                        print('文件处理成功 %s' % x)
                    else:
                        pass
                        #print('文件处理失败 %s' % x)

                except ValueError as e:
                    pass
                    #print(e)

print(len(danlist))
#print(danlist)


with open('需求汇总.txt', 'w',encoding='utf-8') as f:
    for dan in danlist:
        print(dan)
        #print(','.join(dan))
        f.writelines('|'.join(dan))
        f.writelines('\n')
        
            




        