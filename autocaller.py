import socket
import subprocess
import threading
from time import sleep


def run_call():
    p = subprocess.Popen('./docker-entrypoint.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 9001))
s.listen(3)
while True:
    c, addr = s.accept()
    data = c.recv(1024)
    if data == b"ding":
        print("begin ring")
        x = threading.Thread(target=run_call)
        x.start()
    elif data == b"ping":
        c.send(b"pong")
    c.close()
