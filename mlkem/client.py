import socket
import time


def send_message(client_socket,message_send):
    client_socket.send (message_send.encode("utf-8"))

def recv_message(client_socket):
    message_recv = ""
    while True:
        msg = client_socket.recv(100)
        if len(msg) <= 0: #aumentar connection timeout
            print("no message received")
            break
        message_recv += msg.decode("utf-8")
        break

    return message_recv

def main():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #host = '192.168.122.165'
    host = socket.gethostname() 
    port= 5050

    client_socket.connect((host, port))

    received_message = ""

    while True:
        
        #primer mensaje
        received_message = recv_message(client_socket)
        print("received:", received_message)

        message_send = "mensaje de cliente 1"
        send_message(client_socket,message_send)
        print(f"sent: {message_send}")

        #segundo mensaje
        received_message = recv_message(client_socket)
        print("received:", received_message)

        message_send = "mensaje de cliente 2"
        send_message(client_socket,message_send)
        print(f"sent: {message_send}")

        break
       








if __name__ == '__main__':
    main()
