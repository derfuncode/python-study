#f = open('testfile.txt','w')

set1 = set()
comtypelist = []


with open('2018-03-09_SZ--222.txt','r') as f1:
    str = f1.readline()
    while str !='':
        list1 = str.split('|')
        if(len(list1) > 2 ):
            if (list1[2] not in comtypelist):
                comtypelist.append(list1[2])
        setitem = ''
        for item in list1[2:]:
            setitem = setitem + '|'+ item 
        #setitem = setitem+'\n'
        set1.add(setitem)
        str = f1.readline()

with open('2018-03-09_SZ--333.txt','w') as f2:
    for s in set1:
        f2.write(s)


print(len(comtypelist))
print(len(set1))
