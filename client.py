# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:04:43 2015

@author: Ray
Client application for the PyChat client
"""

import socket

# create the socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get hostname
host = socket.gethostname()
port = 9998

# connect to the server
clientSocket.connect((host, port))

# receive 1024 bytes
msg = clientSocket.recv(1024)

clientSocket.close()

print "The message from the server was: %s" % msg.decode("ascii")