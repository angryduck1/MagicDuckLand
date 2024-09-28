from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from DuckLandLogic.Player import Player
from DuckLandLogic.Message.Alliance.AllianceListMessage import *


class SearchAlliancesMessage(PiranhaMessage):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        self.stream.readString()

    def getMessageType(self) -> int:
        return 14324