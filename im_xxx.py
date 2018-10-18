#pip install pypiwin32
#pip install python-docx
#查找指定目录的需求概要设计并查出所有出现过的IM_XXX接口
# 升级pip版本 python -m pip install --upgrade pip

import docx
import os
import re
from win32com import client as wc

strpath = 'D:\\工作\\月度工作\\2018年\\2018年10月\\SNV18.10.0\\SNV18.10.0_需求交付文档\\'


#将doc文件全部转为docx文件
word = wc.Dispatch('Word.Application')
#os.mkdir(strpath+"docx")

for x in os.listdir(strpath):
    if os.path.isfile(strpath+x):
        fname,suffix=os.path.splitext(x)  
        if suffix == ".doc":
            doc = word.Documents.Open(strpath+x)
            doc.SaveAs(strpath+ x + "x", 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件     
            doc.Close()

word.Quit()

#对每一个docx文件进行正则查询匹配
pattern = re.compile(r'[a-zA-Z]{3,6}\_IM\_\d{3,4}')

for x in os.listdir(strpath):
    if os.path.isfile(strpath+x):
        fname,suffix=os.path.splitext(x)  
        if suffix == ".docx":
            file = docx.Document(strpath+x)
            imset = set()
            for para in file.paragraphs:
                match = pattern.findall(para.text)
                if match:
                    imset = imset.union(set(match))
            if(len(imset) > 0):
                print(re.search(r'BR\d{12}',x).group(),",",x,",",imset)        


