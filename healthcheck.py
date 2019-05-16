import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9001))
s.send(b"ping")
msg = s.recv(1024)
if msg != b"pong":
    raise Exception("BROKEN")
print("happy")
