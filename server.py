import socket
import uuid


HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(5)

def randomID():
    random_uuid = uuid.uuid4()
    return random_uuid


print('Initiating server address...........')

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f'Message from the client is: {message}')

    communication_socket.send(f'\nYour id is: {randomID()}'.encode('utf-8'))
    communication_socket.send('\nGot you message thank you'.encode('utf-8'))
    communication_socket.close()
    print(f"Communication with {address} ended!")