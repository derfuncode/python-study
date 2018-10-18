#f=open('break.pl','r')

with open('break.pl','r') as f:
    #linelist = list(f)
    linelist = f.readlines()
    print(len(linelist))
    for x in range(len(linelist)):
        print(linelist[x],end='')




