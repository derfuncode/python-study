sqlist = []
with open(r'C:\Users\caodefang\Documents\python\cardscope.txt','r') as f0:
    strline = f0.readline()
    lineno = 0
    while strline != '':
        strline = strline.strip('\n') 
        start,end = strline.split('\t')
        for i in range(0,int(end)-int(start)+1):
            sqlist.append((int(start)+i))
        lineno = lineno+1
        print(str(lineno)+":"+start+" "+end+":"+str(int(end)-int(start)+1))
        strline = f0.readline()
        

with open(r'C:\Users\caodefang\Documents\python\scopelist.txt','w') as f1:
    for sq in sqlist:
        f1.write(str(sq)+'\n')

