# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:54:13 2015

@author: Ray
Server application for the PyChat client
"""

import socket
import select
#import time

def broadcastMessage(sock, message):
    # do not send the message to the server or the client that sent the message
    for socket in CONNECTION_LIST:
        if socket != serverSocket and socket != sock:
            try:
                socket.send(message)
            except:
                # unable to connect to the socket for some reason
                socket.close()
                CONNECTION_LIST.remove(socket)

# a list of all current, active connections to the server
CONNECTION_LIST = []

# buffer to receive messages into
RECV_BUFFER = 4096

# create the socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serverSocket = socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# get hostname
# host = socket.gethostname()
port = 9998

# bind to all local IP addresses on the specific port
serverSocket.bind(("0.0.0.0", port))

# queue up to 10 requests at a time
serverSocket.listen(10)

# add the server to the list of active connections
CONNECTION_LIST.append(serverSocket)

while True:
    # get the list of currently readable sockets from select()
    readSockets, writeSockets, errorSockets = select.select(CONNECTION_LIST, [], [])
 
    for sock in readSockets:
        # new connections
        if sock == serverSocket:
            clientSocket, clientAddr = serverSocket.accept()
            CONNECTION_LIST.append(clientSocket)
            print "Client (%s, %s) connected!" % clientAddr
            broadcastMessage(clientSocket, "[%s:%s] has entered the room.\n" % clientAddr)
        # incoming message from a client
        else:
            try:
                data = sock.recv(RECV_BUFFER)
                if data:
                    broadcastMessage(sock, "\r" + "<" + str(sock.getpeername()) + "> " + data)
            except:
                broadcastMessage(sock, "Client (%s, %s) is offline" % clientAddr)
                print "Client (%s, %s) is offline" % clientAddr
                sock.close()
                CONNECTION_LIST.remove(sock)
                continue
     
serverSocket.close()