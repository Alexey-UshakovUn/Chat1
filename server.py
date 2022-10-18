import socket
import threading


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 1234))

server_socket.listen()
print("Server is listening")

clients = []


def send_all(data, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(data)


def listen_user(client_socket):
    print("Listening user")

    while True:
        data = client_socket.recv(2048)
        if data:
            print(f"User sent {data}")
        else:
            print(client_socket, 'Отключился')
            client_socket.close()
            clients.remove(client_socket)

        send_all(data, client_socket)


def accept_client():
    client_socket, address = server_socket.accept()
    print(f"User <{address}> connected!")
    return client_socket


def start_server():
    while True:
        client_socket = accept_client()

        clients.append(client_socket)

        listen_accepted_user = threading.Thread(
            target=listen_user,
            args=(client_socket,)
        )

        listen_accepted_user.start()


if __name__ == '__main__':
    start_server()
