import socket
import time

def send_message(client_socket,message_send):
        client_socket.send (message_send.encode("utf-8"))  

def recv_message(client_socket):
    message_recv = ""
    while True:
        msg = client_socket.recv(100)
        if len(msg) <= 0:
            print("no message received")
            break
        message_recv += msg.decode("utf-8")
        break
    return message_recv

def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname() 
    #host = '192.168.122.165'
    port = 5050
    server_socket.bind((host, port))
    server_socket. listen (5)
    print(f"Connection with server established")
    
    client_socket,address = server_socket.accept()
    received_message = ""

    while True:
        #primer mensaje
        message_send = "mensaje de servidor 1"
        send_message(client_socket,message_send)
        print(f"sent: {message_send}")

        received_message = recv_message(client_socket)
        print("received: ", received_message)

        #seundo mensaje
        message_send = "mensaje de servidor 2"
        send_message(client_socket,message_send)
        print(f"sent: {message_send}")
    
    
        received_message = recv_message(client_socket)
        print("received: ", received_message)
        #print(len(received_message))

        client_socket.close()
        break

if __name__ == '__main__':
    main()





    
    