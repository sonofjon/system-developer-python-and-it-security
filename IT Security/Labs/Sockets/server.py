import socket

BUFSIZE = 16
PORT = 5050
FORMAT = 'utf-8'

host_name = socket.gethostname()
server_name = socket.gethostbyname(host_name)
addr = (server_name, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(addr)
    print("[STARTING] server is starting...")
    s.listen()
    print(f"[LISTENING] Server is listening on {server_name}")

    while True:
        conn, addr = s.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        while True:
            msg = conn.recv(BUFSIZE).decode(FORMAT)
            if msg == '':
                break

            print(f"[{addr}] {msg}")

        conn.close()