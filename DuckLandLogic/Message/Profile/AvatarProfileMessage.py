from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from DuckLandLogic.Avatar.LogicClientAvatar import LogicClientAvatar

class AvatarProfileMessage(PiranhaMessage):

    def __init__(self):
        super().__init__(0)
    
    def encode(self):
        LogicClientAvatar().encode(self.stream)
    
    def getMessageType(self):
        return 24334