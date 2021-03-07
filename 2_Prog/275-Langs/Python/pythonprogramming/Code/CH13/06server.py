# The server
import socket

HOST = '' # A null string is ok here.
PORT = 50007
s = socket.socket(socket.AF_INET, \ 
      socket.SOCK_STREAM)
s.bind ((HOST, PORT))
s.listen()
conn, addr = s.accept()
data = conn.recv(1024)
print ("Server heard '", data, "'")
conn.send (b'Hello. Nice to see you.')
while True:
# Read the incoming data
    data = conn.recv(1024)                     
    if data:
# Convert it to integer
        i = int(data)        
        print ("Received ", i)
# Square it and convert to bytes
        data = str(i*i).encode() 
# Send to the client   
        conn.send (data)            
   conn.close()