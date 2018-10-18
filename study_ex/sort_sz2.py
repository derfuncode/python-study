prodlist = []
with open(r'D:\Users\caodefang\python\999prod.txt','r') as f0:
    prod = f0.readline()
     
    while prod != '':
        prod = prod.strip('\n') 
        prodlist.append(prod)
        prod = f0.readline()

print(prodlist)

with open(r'D:\工作\月度工作\2018年\2018年4月\流量长市漫\DQ_AA_20180313_6246784.txt','r') as f1:
    with open(r'D:\工作\月度工作\2018年\2018年4月\流量长市漫\DQ_AA_20180313_6246784_755_2.txt','w') as f2:
        str = f1.readline()
        while str !='':
            #if str.find('深圳') >=0:
            for pd in prodlist:
                if str.find(pd) >=0:
                    f2.write(str)
                    break
                
            str = f1.readline()