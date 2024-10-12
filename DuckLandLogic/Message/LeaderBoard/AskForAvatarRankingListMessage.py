from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from DuckLandLogic.Player import Player
from DuckLandLogic.Message.LeaderBoard.AvatarRankingListMessage import AvatarRankingListMessage

class AskForAvatarRankingListMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)

    def decode(self):
        if self.stream.readBoolean():
            self.stream.readLong()

    def getMessageType(self):
        return 14403