# -*- coding: utf-8 -*-：
import os
import sys
import pickle
import re
import  codecs
import string
import shutil
from win32com import client as wc


strpath = 'D:\\工作\\月度工作\\2018年\\2018年5月\\V18.4.0\\概要设计_V18.5.0\\NG\\'

word = wc.Dispatch('Word.Application')
#os.mkdir(strpath+"docx")

for x in os.listdir(strpath):
    if os.path.isfile(strpath+x):
        fname,suffix=os.path.splitext(x)  
        if suffix == ".doc":
            doc = word.Documents.Open(strpath+x)
            #print(strpath+"docx\\"+x + "x")
            print(strpath +x + "x")
            #doc.SaveAs(strpath+"docx\\"+x + "x", 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件 
            doc.SaveAs(strpath+ x + "x", 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件     
            doc.Close()

word.Quit()