import socket

port = 25500

s = socket.socket()
s.bind(('0.0.0.0', port))

print("Socket has been binded to port " + str(port))
s.listen(3)
print("Socket is now listening for keys to be verified")

while True:
    c, addr = s.accept()
    print("Received a connection from " + addr)
    print(c.recv(1024))
    c.close()