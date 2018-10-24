with open(r'C:\Users\caodefang\Documents\github\free-python-games\requirements.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


