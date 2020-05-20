import socket

s = socket.socket()
print 'Socket Connected'
s.bind(('localhost', 9999))
s.listen(3)
print 'waiting for connections'
while True:
    c, address = s.accept()
    name = c.recv(1024).decode()
    print 'Connection with address ', address , name
    c.send(bytes('Welcome to Python '))
    c.close()
