import socket
import time

def send_message(client_socket,message_send):
    client_socket.send (message_send.encode("utf-8"))
    print(f"sent: {message_send}")

def recv_message(client_socket):
    message_recv = ""
    while True:
        msg = client_socket.recv(100)
        if len(msg) <= 0:
            print("no message received")
            break
        message_recv += msg.decode("utf-8")
        print("received:", message_recv)
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


    while True:

        #primer mensaje
        message_send = "mensaje de servidor 1"
        send_message(client_socket,message_send)
        recv_message(client_socket)

        #seundo mensaje
        message_send = "mensaje de servidor 2"
        send_message(client_socket,message_send)

        #seguridad
        received_message = recv_message(client_socket)
        sent_message = send_message(client_socket,message_send)
        if not received_message or not sent_message:
            break

        client_socket.close()





if __name__ == '__main__':
    main()





    
    