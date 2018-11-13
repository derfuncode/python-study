# 遍历指定目录的需求分工excel文件，获取全量去重后的分工表
import os
import xlrd
import csv
import json
import re
import time

danlist = []
strpath = 'd:\\工作\\月度工作\\2018年\\2018年11月\\SNV18.11.0\\2018分工\\'
for x in os.listdir(strpath):
    fname, suffix = os.path.splitext(x)
    if suffix == ".xlsx" or suffix == ".xls":
        wb = xlrd.open_workbook(strpath + x)
        for name in wb.sheet_names():
            s = wb.sheet_by_name(name)
            if s.nrows > 0:
                cellvalue = s.row_values(0)
                try:
                    chargename = -1
                    danid = -1
                    danname = -1
                    danver = -1
                    for index in range(len(cellvalue)):
                        if '深圳负责人' in str(cellvalue[index]):
                            chargename = index
                        if '单号' in str(cellvalue[index]):
                            danid = index
                        if '需求名称' in str(cellvalue[index]):
                            danname = index
                        if '版本' in str(cellvalue[index]):
                            danver = index
                    if chargename >= 0 and danid >= 0 and danname >= 0:
                        for i in range(s.nrows-1):
                            cell = s.row_values(i+1)
                            if re.match(r'BR\d{12}', cell[danid]):
                                if danver >= 0:
                                    ver = cell[danver]
                                else:
                                    ver = ''
                                danlist.append([str(cell[danid]).strip().replace('\n', ''), str(cell[danname]).strip().replace(
                                    '\n', ''), str(ver).strip().replace('\n', ''), str(cell[chargename]).strip().replace('\n', ''), x])
                        print('文件处理成功 %s' % x)
                    else:
                        pass
                except ValueError as e:
                    pass

print(len(danlist))

with open(strpath+'需求汇总'+time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '.txt', 'w', encoding='utf-8') as f:
    for dan in danlist:
        f.writelines('|'.join(dan))
        f.writelines('\n')
