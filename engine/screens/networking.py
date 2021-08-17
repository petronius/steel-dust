
from PodSixNet.Connection import ConnectionListener, connection


class ClientConnectionListener(ConnectionListener):

    def __init__(self, level):
        self.level = level
        self.Connect((level.game.host, level.game.port))
        self.Pump()
        print("Client connection initiated")

    def Network(self, data):
        pass
        #print("Network:", data)

    def Network_players(self, data):
        print("*** players: %s" % data)
        self.level.update_players(data)

    def Network_connected(self, data):
        print("Connection successful!", data)

    def Network_error(self, data):
        print('error:', data['error'])
        connection.Close()
        raise RuntimeError("Connection failed!")

    def Network_disconnected(self, data):
        print('Server disconnected:', data)
        connection.Close()
        raise RuntimeError("Connection failed!")
