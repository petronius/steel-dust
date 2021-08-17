
from PodSixNet.Connection import connection, ConnectionListener


class ClientConnectionListener(ConnectionListener):

    def __init__(self, level):
        self.level = level
        self.Connect((level.game.host, level.game.port))
        self.update()
        print("Client connection initiated")

    def Network(self, data):
        print("Network:", data)

    def Network_players(self, data):
        print("*** players: " + ", ".join([p.get("name") for p in data['players']]))
        self.level.update_players(data)

    def Network_message(self, data):
        print(data['who'] + ": " + data['message'])

    def Network_connected(self, data):
        print("Connection successful!", data)

    def Network_error(self, data):
        print('error:', data['error'])
        connection.Close()
        raise RuntimeError("Connection failed!")

    def Network_disconnected(self, data):
        print('Server disconnected:', data)

    def Network_playerconnect(self, data):
        print("New player has joined:", data)
        self.level.player_connect(data)

    def update(self):
        self.Pump()
        connection.Pump()
