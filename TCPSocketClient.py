import socket
import clipboard
import time

class TCPSocketClient():
    def __init__(self, ip, port):
        print "TCPSocketClient init"
        self.ip = ip
        self.port = port
        self.data = ""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, self.port))

    def get_clipboard(self):
        data = clipboard.paste()
        return data

    def sendClipboardData(self):
        while (True):
            data = self.get_clipboard()
            if (data != "" and len(data) != len(self.data)):
                #print "data : " + data
                try:
                    if (self.s != 0):
                        self.s.send(data)
                        self.data = data
                except Exception as e:
                    #print e
                    self.s.close()
                    self.s = 0
            else:
                data = ""

            time.sleep(2)
            if (self.s == 0):
                try:
                    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.s.connect((self.ip, self.port))
                except:
                    #print "Cannot connect to server"
                    self.s = 0

    def __del__(self):
        print "TCPSocketClient destroyed"
        self.s.close()

