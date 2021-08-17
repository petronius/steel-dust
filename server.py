import sys


# Get command line argument of server, port
if __name__ == '__main__':
    from engine.server import GameServer

    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
    else:
        host, port = sys.argv[1].split(":")
        s = GameServer(localaddr=(host, int(port)))
        s.Launch()
