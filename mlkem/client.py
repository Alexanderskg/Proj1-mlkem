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

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #host = '192.168.122.165'
    host = socket.gethostname() 
    port= 5050

    client_socket.connect((host, port))

    flag_recv = True

    while True:
        
        if flag_recv == True:
            received_message = recv_message(client_socket)
            flag_recv = False

        send_message(client_socket,"csb")

        received_message = recv_message(client_socket)
        if not received_message:
            break

        client_socket.close()

       








if __name__ == '__main__':
    main()
