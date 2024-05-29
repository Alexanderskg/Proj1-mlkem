import socket 

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((socket.gethostname(), 5050)) #change ip

message = ''

while True:
    msg = socket.recv(8)
    if len(msg) <= 0:
        break
    message += msg.decode("utf-8")

print(msg.decode("utf-8"))