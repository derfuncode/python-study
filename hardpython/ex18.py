def print_two(*args):
    arg1,arg2 = args
    print("arg1:%r,arg2:%r" % (arg1,arg2))

def print_two_again(*args):
    arg1,arg2 = args
    print("arg1:%r,arg2:%r" % (arg1,arg2))

def print_one(arg1):
    print("arg1:%r" % arg1)

def print_none():
    print("i got nothing")

print_two("曹德芳","曹宇轩")

print_two_again("曹德芳","曹宇轩")

print_one("曹宇萌")

print_none()

