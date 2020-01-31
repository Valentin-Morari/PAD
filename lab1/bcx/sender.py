#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The BROKER's hostname or IP address
PORT = 65434        # The port used by the BROKER
CHANNEL = "fna349fn"
MESSAGE_TYPE = "send"
MESSAGE = "hi"
DATA = CHANNEL+MESSAGE_TYPE+MESSAGE

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(DATA.encode())
    data = s.recv(1024)

print('Received')
