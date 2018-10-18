

with open(r'D:\工作\月度工作\2018年\2018年4月\流量长市漫\DQ_AA_20180313_6246784.txt','r') as f1:
    with open(r'D:\工作\月度工作\2018年\2018年4月\流量长市漫\DQ_AA_20180313_6246784_sz.txt','w') as f2:
        str = f1.readline()
        while str !='':
            if str.find('深圳') >=0:
                f2.write(str)
            str = f1.readline()


