from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from DuckLandLogic.Player import Player
from DuckLandLogic.Message.Battles.NpcDataMessage import *

class AttackNpcMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)

    def decode(self):
        self.stream.readInt()

    def process(self):
        NpcDataMessage().Send()

    def getMessageType(self):
        return 14134