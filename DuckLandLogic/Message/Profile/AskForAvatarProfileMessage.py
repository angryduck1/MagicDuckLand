from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from DuckLandLogic.Player import Player
from DuckLandLogic.Message.Profile.AvatarProfileMessage import AvatarProfileMessage

class AskForAvatarProfileMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)
        
    def decode(self):
        self.stream.readInt() # AvatarHighID
        self.stream.readInt() # AvatarLowID
        self.stream.readInt() # HomeHighID
        self.stream.readInt() # HomeLowID

    def getMessageType(self) -> int:
        return 14325