def parrot(voltage,state = 'a stiff', action = 'voom',type = 'norwegian bule'):
    print("-- this parrot wouldn't ", action,end=' ')
    print("if you put", voltage,"volts through it.")
    print("-- lovely plumage, the",type)
    print("-- it's ",state,"!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=100000,action='Vooooom')
parrot(action='voooom',voltage = 100000)
parrot('a million','bereft of life','jump')
parrot('a thousand',state = 'pushing up the daisies')

