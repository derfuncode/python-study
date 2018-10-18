import json
with open('jsonwrite.txt','r') as f:
    x2 = json.load(f)
    for xnode in x2:
        print(xnode)
