
from PodSixNet.Connection import connection, ConnectionListener


class ClientConnection(ConnectionListener):
    def __init__(self, host, port, handle):
        self.Connect((host, port))
        print("Client connection initiated")
        connection.Send({"handle": handle})

    def Pump(self):
        connection.Pump()

    def Network_players(self, data):
        print("*** players: " + ", ".join([p for p in data['players']]))

    def Network_message(self, data):
        print(data['who'] + ": " + data['message'])

    # built in stuff

    def Network_connected(self, data):
        print("Connection successful!")

    def Network_error(self, data):
        print('error:', data['error'][1])
        connection.Close()

    def Network_disconnected(self, data):
        print('Server disconnected')


