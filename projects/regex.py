import re

pattern = re.compile(r'\d+(\.\d*)?')

strtest = "2,0.004,75.0"

match = pattern.findall(strtest)
if match:
    print(match)        

m=re.search('^The', 'The end')
if m:
    print(m.group())

m=re.search('^The', 'end. The')
if m:
    print(m.group())

print(r"test \bthe")
m = re.search(r'\bthe','bite the dog')
if m:
    print(m.group())



