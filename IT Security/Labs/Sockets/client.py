import socket

PORT = 5050
FORMAT = 'utf-8'
SERVER = "192.168.10.143"
FILE = "sample.txt"
ADDR = (SERVER, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(ADDR)
    with open(FILE, mode='rb') as file:
        client.sendfile(file)