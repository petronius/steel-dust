from engine.game import Game
from multiprocessing import Process
import engine.server
import sys

def main(host, port):
    game = Game(host, port)
    game.execute()


if __name__ == "__main__":
    host, port = "localhost",31425
    if len(sys.argv) == 1:
        print("No server specified. Will launch default local server.")
        p = Process(target=engine.server.RunDefaultServer)
        p.start()
    elif len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
        exit()
    else:
        host, port = sys.argv[1].split(":")
    main(host, int(port))
