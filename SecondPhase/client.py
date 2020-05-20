import socket

c = socket.socket()
c.connect(('localhost', 9999))
name = raw_input('Enter a name')
c.send(bytes(name))

print c.recv(1024).decode()
