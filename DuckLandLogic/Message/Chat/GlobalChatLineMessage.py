from DuckLandLogic.Player import Player
from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from DuckLandTitan.Logic.Math.LogicLong import LogicLong
from DuckLandLogic.Avatar.LogicClientAvatar import LogicClientAvatar

class GlobalChatLineMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)

    def encode(self):
        self.stream.writeString("как писать самому?")
        self.stream.writeString("angryduck001")

        self.stream.writeInt(0)
        self.stream.writeInt(0)

        self.stream.writeLong(LogicLong(1, 1))
        self.stream.writeLong(LogicLong(1, 1))

        self.stream.writeBoolean(True)

    def getMessageType(self) -> int:
        return 24715