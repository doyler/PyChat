# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:04:43 2015

@author: Ray
Client application for the PyChat client
"""

import socket

# chat_client.py

import sys
import socket
import select

def send_msg(sock):
    while True:
        data = sys.stdin.readline()
        sock.sendto(data, target)

def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        sys.stdout.write(data)

# create the socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server information
host = "127.0.0.1"
port = 9998

# set a timeout of 2 seconds for the socket
clientSocket.settimeout(2)

# connect to the server
try:
    clientSocket.connect((host, port))
except:
    print "Error connecting to the server."
    sys.exit()
    
print "Connected to the remote host, you can now start sending messages."

sys.stdout.write('[Me] '); sys.stdout.flush()

while True:
    socketList = [sys.stdin, clientSocket]
    
    # get the list of currently readable sockets from select()
    readSockets, writeSockets, errorSockets = select.select(socketList, [], [])
    
    for sock in readSockets:
        # incoming message from the server
        if sock == clientSocket:
            data = sock.recv(4096)
            if not data:
                print "\nDisconnected from the chat server."
                sys.exit()
            else:
                
                sys.stdout.write(data)
                sys.stdout.write('[Me] '); sys.stdout.flush() 
        # outgoing message to the server
        else:
            message = sys.stdin.readline()
            clientSocket.send(msg)
            sys.stdout.write('[Me] '); sys.stdout.flush() 

"""
# connect to the server
clientSocket.connect((host, port))

# receive 1024 bytes
msg = clientSocket.recv(1024)

clientSocket.close()

print "The message from the server was: %s" % msg.decode("ascii")
"""