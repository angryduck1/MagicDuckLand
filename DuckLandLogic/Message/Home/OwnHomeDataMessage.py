from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from DuckLandLogic.Avatar.LogicClientAvatar import LogicClientAvatar
from DuckLandLogic.Home.LogicClientHome import LogicClientHome

class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self) -> None:
        super().__init__(0)
        self.clientHome = LogicClientHome()
        self.clientAvatar = LogicClientAvatar()

    def getMessageType(self) -> int:
        return 24101

    def encode(self):
        super().encode()
        self.stream.writeInt(0)
        self.clientHome.encode(self.stream)
        self.clientAvatar.encode(self.stream)