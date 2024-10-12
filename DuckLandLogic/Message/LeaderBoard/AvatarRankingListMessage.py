from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from DuckLandLogic.Player import Player

class AvatarRankingListMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)
    
    def encode(self):
        self.stream.writeInt(1)

    def getMessageType(self):
        return 24403