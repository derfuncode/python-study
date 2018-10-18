s= 'hello,world.'
print(str(s))
print(repr(s))

print(str(1/7))
print(repr(1/7))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

