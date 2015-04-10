# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:54:13 2015

@author: Ray
Server application for the PyChat client
"""

import socket
import time

# create the socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get hostname
host = socket.gethostname()
port = 9998

# bind to the port
serverSocket.bind((host, port))

# queue up to 5 requests
serverSocket.listen(5)

while True:
    # establish the connection
    clientSocket, clientAddr = serverSocket.accept()
    
    print "Got a connection from %s" % str(clientAddr)
    currentTime = time.ctime(time.time()) + "\r\n"
    clientSocket.send(currentTime.encode("ascii"))
    clientSocket.close()