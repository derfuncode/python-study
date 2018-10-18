import os
import hashlib
import time


def md5_calc(file):        
    md5_value=hashlib.md5()
    with open(file,'rb') as file_b:
        while True:
            data_flow=file_b.read(8096)       #每次读入8089kb进入内存
            if not data_flow:                 #读取完后返回空值，False
                break
            md5_value.update(data_flow)
    file_b.close()
    return md5_value.hexdigest()

duphash = dict()


def listDir(rootDir):
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if (os.path.isfile(pathname)):
            strmd5 = md5_calc(pathname)
            #print(pathname,":",strmd5)
            if (strmd5 in duphash):
                listfile = duphash[strmd5]
                listfile.append(pathname)
                duphash[strmd5] = listfile
            else:
                listfile = []
                listfile.append(pathname)
                duphash[strmd5] = listfile

        else:
            listDir(pathname)

root = "D:\\工作\\"
listDir(root)


with open(root+"dupfile"+time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time())) +'.txt', 'w',encoding='utf-8') as f:
    for key in duphash:
        if(len(duphash[key])>1):
            f.writelines(key)
            f.writelines('|')
            f.writelines(str(len(duphash[key])))
            f.writelines('|')
            for fn in duphash[key]:
                f.writelines(fn)
                f.writelines(',')
            f.writelines('\n')

