import sys
from time import sleep, localtime
from weakref import WeakKeyDictionary
import logging

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


class GameServer(Server):

    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.players = WeakKeyDictionary()
        logging.info('Server launched')

    def Connected(self, channel, addr):
        self.AddPlayer(channel)
        logging.info("connected: %s (waiting for player initialization)" % str(addr))

    def AddPlayer(self, player):
        print("New Player %s (%s)" % (player, str(player.addr)))
        self.players[player] = True
        logging.info("players", [p for p in self.players])

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
        [p.Send(data) for p in self.players]

    def Launch(self):
        while True:
            self.Pump()
            sleep(0.0001)


def RunDefaultServer():
        host, port = "localhost", 31425
        s = GameServer(localaddr=(host, port))
        s.Launch()
