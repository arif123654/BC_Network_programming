import socket
import threading
import uuid


HOST = '127.0.0.1'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()


clients = []
nicknames = []


def broadCast(msg):
    for client in clients:
        client.send(msg)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(message)
            broadCast(message)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()

            nickname = nicknames[index]
            broadCast(f"{nickname} has left the chat!".encode('ascii'))
            nicknames.remove(nickname)


def receive():
    while True:
        print('Receiving messages from the clients................')
        client,addr = server.accept()
        print(f'Accept with {addr}')

        name = "NICKNAME"
        client.send(name.encode('ascii'))

        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f'\nNickname of the connection client is: {nickname}')
        broadCast(f"\n{nickname} has newly joined the chat!")

        client.send("\nConnected to the server!".encode('ascii'))

        thread = threading.Thread(target=handle, args=(clients,))


print('\nServer is up and running')
receive()