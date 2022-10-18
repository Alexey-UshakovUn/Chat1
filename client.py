import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))


def receive_data():
    while True:
        data = client_socket.recv(1024)
        print(_decode(data))
        send_data()


def _decode(data: bytes):
    return data.decode()


def _encode(data: str):
    return data.encode()


def send_data():
    data = input_message()
    client_socket.send(_encode(data))


def input_message():
    data = input('data: ')
    return data


if __name__ == "__main__":
    receive_data()
