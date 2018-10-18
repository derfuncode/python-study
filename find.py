# coding=utf-8
import os
import sys

# 找到当前目录下的所有文本文件


def findFile(path):
    f = []
    d = []
    l = os.listdir(path)
    for x in l:
        if os.path.isfile(os.path.join(os.getcwd() + "\\", x)):
            f.append(x)
        else:
            d.append(x)
    return f, d  # 返回文件和目录的列表
# print x, "\n", y

# 统计一个文本内字符串的个数


def findstrCount(file, strToFind):
    count = 0
    thefile = open(file, 'rb')
    while True:
        buffer = thefile.read()
        if not buffer:
            break
        count += buffer.count(strToFind)
    thefile.close()
    return count

# 遍历文件列表中，包含特定字符串的文件


def findstr(file, str):
    # f = open(file, "r+")
    # if f.read().find(str) != -1:
    #     s = os.getcwd() + "\\" + file
    # else:
    #     s = "None"
    # f.close()
    i = 1
    global s

    for line in open(file):
            # return is index of the str start position.
        if line.find(str) != -1:
            s = os.getcwd() + "\\" + file + "------>line:%d" % (i)
            print s
        i = i + 1
    return s

L = []  # 全局变量，存放找到的目标文件


def find(p, str):
    try:
        f, d = findFile(p)
        for x in f:
            Ret = findstr(x, str)
            if Ret:
                L.append(Ret)
        if d:
            for x in d:
                os.chdir(x)
                find("./", str)
                os.chdir('../')
    except Exception, e:
        print e
    finally:
        pass

if __name__ == '__main__':
    s = 0
    find(sys.argv[1], sys.argv[2])