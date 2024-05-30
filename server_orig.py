import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname() 
#host = '192.168.122.165'
port = 5050

server_socket.bind((host, port))

server_socket. listen (5)
print(f"Connection with server established")


message_send = "Hello client"

while True:

    clientsocket, address = server_socket.accept()
    clientsocket.send (message_send.encode("utf-8"))

    #time.sleep(1)
    message_recv = ''
    msg= clientsocket.recv(16)
    if len(msg)<=0:
        break
    message_recv += msg.decode("utf-8")

    print(message_recv)


    clientsocket.close()
    
    