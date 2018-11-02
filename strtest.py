str = "17429191486168765	17429191486168789"
start,end = str.split('\t')

for i in range(0,int(end)-int(start)+1):
    print(int(start)+i)

print("ssdf")