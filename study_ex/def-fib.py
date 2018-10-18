def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b = b,a+b
    print()

fib(2000)

print(fib)
f = fib

print(f)

f(100)