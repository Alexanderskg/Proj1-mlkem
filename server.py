import socket 

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((socket.gethostname()),5050) #change ip
socket.listen(5)

while True:
    clientsocket, address = socket.accept()
    print(f"Connection with server established")
    clientsocket.send(bytes("Test string") , "utf-8")
    clientsocket.close()
    
