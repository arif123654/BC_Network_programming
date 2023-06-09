import socket



HOST = '127.0.0.1'
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

client.send("Hello world".encode('utf-8'))

received_message = client.recv(1024).decode('utf-8')

print(f'Message from server: {received_message}')

client.close()
