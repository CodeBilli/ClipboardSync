import socket
import SocketServer
import clipboard
import time

class TCPSocketServer():
    def __init__(self, ip, port):
        print "TCPSocketServer init"
        # Create the server, binding to localhost on port 9999
        self.server = SocketServer.TCPServer((ip, port), self.tcpHandler)

    def start(self):
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        self.server.serve_forever()

    def tcpHandler(self, r, ca, s):
        while 1:
            try:
                #print "Waiting for data from the client : " + ca[0] + "..."

                # self.request is the TCP socket connected to the client
                size = r.recv(8192, socket.MSG_PEEK)
                #print len(size)
                if (len(size) == 0):
                    break

                if (len(size) < 8192):
                    self.data = r.recv(len(size)).strip()
                else:
                    temp = len(size)
                    while (temp > 0):
                        self.data += r.recv(8192).strip()
                        temp -= 8192

                #print self.data

                # Copy this data to clipboard
                clipboard.copy(self.data)

                time.sleep(2)
            except Exception as e:
                print e
                self.server.shutdown()


    def __del__(self):
        print "TCPSocketServer destroyed"
        self.s.close