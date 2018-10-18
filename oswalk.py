import os
root = "D:\\Users\\caodefang\\Documents\\python\\"

for dirpath, dirnames, filenames in os.walk(root):
    for filepath in filenames:
        print(os.path.join(dirpath, filepath))