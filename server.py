import socket



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 9999))
server_socket.listen()


def accept_connection():
    while True:
        client_socket, addr = server_socket.accept()
        print('Connection from:', addr)
        client_socket.send('hello'.encode())
        receive_message(client_socket)


def receive_message(client_socket: socket.socket):
    while True:
        data = client_socket.recv(1024)
        print(data.decode())
        if data:
            send_message(client_socket)


def send_message(client_socket: socket.socket):
    data = 'Hello'
    client_socket.send(data.encode())
    print('message send')


if __name__ == '__main__':
    accept_connection()
