# Echo client program
import socket

HOST = '192.168.rr.xxx'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'Hi there!')
data = s.recv(1024)
print ("Client heard '", str(data), "'")
for i in range (0, 100):
    data = str(i).encode()
    s.send (data)
    data = s.recv(1024)
    print ("Sent ", i, " received ", data)
s.close()

