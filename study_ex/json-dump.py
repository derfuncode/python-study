import json
squarex = [(x, x**2) for x in range(10)]

with open('jsonwrite.txt','w') as f:
    json.dump(squarex,f)

