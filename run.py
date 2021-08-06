from engine.game import Game
import sys

def main(host, port):
    game = Game(host, port)
    game.execute()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
    else:
        host, port = sys.argv[1].split(":")
        main(host, int(port))
