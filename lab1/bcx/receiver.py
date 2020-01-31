#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65469        # Port for RECEIVER

BHOST = '127.0.0.1'  # The BROKER's hostname or IP address
BPORT = 65434        # The port used by the BROKER

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((BHOST, BPORT))
    data = s.sendall(b"listen")
    data = s.recv(1024)
