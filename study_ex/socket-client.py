import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('10.245.6.246',9999))

print(s.recv(1024).decode('utf-8'))

for data in [b'caodefang',b'linyuxing',b'xujichen']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

