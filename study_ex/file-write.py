#f = open('testfile.txt','w')

set1 = set()

with open('2018-03-09_SZ--222.txt','r') as f1:
    str = f1.readline()
    while str !='':
        set1.add(str[19:])
        str = f1.readline()

with open('2018-03-09_SZ--333.txt','w') as f2:
    for s in set1:
        f2.write(s)
