import sys
import TCPSocketClient
import TCPSocketServer

def main():
    print "Hello Clipboard Sync!"

    # Read the command line arg to determine whether this be server or client...
    if len(sys.argv) < 4:
        print "Usage : ClipboardSync server/client ip port"
        sys.exit(1)

    if sys.argv[1] == "server":
        print "Creating a Socket Server"
        ip = sys.argv[2]
        port = sys.argv[3]
        ss = TCPSocketServer.TCPSocketServer(ip, int(port))
        ss.start()
    elif sys.argv[1] == "client":
        print "Creating a Socket Client"
        ip = sys.argv[2]
        port = sys.argv[3]
        cs = TCPSocketClient.TCPSocketClient(ip, int(port))
        cs.sendClipboardData()
    else:
        print "Unknown option"
        sys.exit(1)

if __name__ == '__main__':
    main()