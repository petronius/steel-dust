import sys
from time import sleep, localtime
from weakref import WeakKeyDictionary

from PodSixNet.Server import Server
from PodSixNet.Channel import Channel

# This is the server representation of a single connected client
class ClientChannel(Channel):
    def __init__(self, *args, **kwargs):
        self.nickname = "anonymous"
        Channel.__init__(self, *args, **kwargs)

    def Close(self):
        self._server.DelPlayer(self)

    def Network_message(self, data):
        self._server.SendToAll({"action":"message","message":data["message"], "who":self.nickname})

    def Network_nickname(self, data):
        self.nickname = data["nickname"]
        self._server.SendPlayers()

class ChatServer(Server):
    channelClass = ClientChannel
    
    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.players = WeakKeyDictionary()
        print('Server launched')
    
    def Connected(self, channel, addr):
        self.AddPlayer(channel)
        print("connected")

    def AddPlayer(self, player):
        print("New Player" + str(player.addr))
        self.players[player] = True
        self.SendPlayers()
        print("players", [p for p in self.players])
        
    def DelPlayer(self, player):
        print("Deleting Player" + str(player.addr))
        del self.players[player]
        self.SendPlayers()
    
    def SendPlayers(self):
        self.SendToAll({"action": "players", "players": [p.nickname for p in self.players]})
        
    def SendToAll(self, data):
        [p.Send(data) for p in self.players]
    
    def Launch(self):
        while True:
            self.Pump()
            sleep(0.0001)
            
# Get command line argument of server, port
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
    else:
        host, port = sys.argv[1].split(":")
        s = ChatServer(localaddr=(host, int(port)))
        s.Launch()