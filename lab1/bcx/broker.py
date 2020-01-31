    #!/usr/bin/env python3

import socket
import _thread

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65434        # Port to listen on (non-privileged ports are > 1023)


CHANNELS = {"fna349fn":[['127.0.0.1', 65469]]}

def on_new_client(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        #do some checks and if msg == someWeirdSignal: break:
        print (addr, ' >> ', msg)
        msg = raw_input('SERVER >> ')
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.send(msg)
    clientsocket.close()



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
            s.listen(9)
            conn, addr = s.accept()
            while conn:
                print('Connected by', addr)
                data = conn.recv(1024)
                if data.decode() == "listen":
                    _thread.start_new_thread(on_new_client,(conn,addr))                    
                for channel in CHANNELS.keys():
                   if data.decode().startswith(channel):
                      print ("found client! on", addr)                
                conn.close()
                conn = None
