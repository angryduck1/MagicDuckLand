from DuckLandLogic.Player import Player
from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from DuckLandTitan.Logic.Math.LogicLong import LogicLong
from DuckLandLogic.Avatar.LogicClientAvatar import LogicClientAvatar

class GlobalChatLineMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)
        self.message = ""

    def setMessage(self, message: str) -> None:
        self.message = message

    def encode(self):
        self.stream.writeString(self.message)
        self.stream.writeString(LogicClientAvatar().encode(self.stream))

        self.stream.writeInt(0)
        self.stream.writeInt(0)

        self.stream.writeLong(LogicLong(0, 1))
        self.stream.writeLong(LogicLong(0, 1))

        self.stream.writeBoolean(True)

    def getMessageType(self) -> int:
        return 24715