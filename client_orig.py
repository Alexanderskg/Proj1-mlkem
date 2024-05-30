import socket
import time
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.122.165'
host = socket.gethostname() 
port= 5050

client_socket.connect((host, port))

message_recv = ''
message_send = "Hello server" 

while True:
    msg = client_socket.recv(16)
    if len(msg) <= 0:
        break
    message_recv += msg.decode("utf-8" )
    print(message_recv)
    
    #time.sleep(1)
    client_socket.send(message_send.encode("utf-8"))
    

client_socket.close()