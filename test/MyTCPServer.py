#!/usr/bin/env python
# coding=utf-8

from SocketServer import TCPServer , ForkingMixIn , StreamRequestHandler

class MyTCPServer(TCPServer, ForkingMixIn):
    pass

