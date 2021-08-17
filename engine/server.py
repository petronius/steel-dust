from time import sleep
from weakref import WeakKeyDictionary

from PodSixNet.Server import Server
from PodSixNet.Channel import Channel


# This is the server representation of a single connected client
class ClientChannel(Channel):

    def __init__(self, *args, **kwargs):
        self.name = "anonymous"
        self.uuid = ""
        self.position = (0, 0)
        Channel.__init__(self, *args, **kwargs)

    def Close(self):
        self._server.DelPlayer(self)

    def Network_playerconnect(self, data):
        self.name = data.get("name", "(unk)")
        self.uuid = data.get("uuid", "(unk)")
        self.position = data.get("position", (200, 200))
        print("Channel initialized for player: %s" % data)
        self._server.SendPlayers()

    def Network_position(self, data):
        print("%s position update being broadcast: %s" % (self.uuid, self.position))
        self.position = data.get("position")
        self._server.SendToOthers(self, data)


class GameServer(Server):

    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.players = WeakKeyDictionary()
        print('Server launched')

    def Connected(self, channel, addr):
        self.AddPlayer(channel)
        print("connected: %s (waiting for player initialization)" % str(addr))

    def AddPlayer(self, player):
        print("New Player %s (%s)" % (player, str(player.addr)))
        self.players[player] = True
        print("players", [p for p in self.players])

    def DelPlayer(self, player):
        print("Deleting Player" + str(player.addr))
        del self.players[player]
        self.SendPlayers()

    def SendPlayers(self):
        # don't send players that aren't fully initialized yet
        players = filter(lambda p: p.uuid not in ("", "(unk)"), self.players)
        self.SendToAll({
            "action": "players",
            "players": [{
                "name": p.name,
                "uuid": p.uuid,
                "position": p.position,
            } for p in players]
        })

    def SendToAll(self, data):
        for p in self.players:
            p.Send(data)

    def SendToOthers(self, sender, data):
        for p in self.players:
            if p.uuid != sender.uuid:
                p.Send(data)

    def Launch(self):
        while True:
            self.Pump()
            sleep(0.0001)


def RunDefaultServer():
        host, port = "localhost", 31425
        s = GameServer(localaddr=(host, port))
        s.Launch()
