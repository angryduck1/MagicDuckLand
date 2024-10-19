from DuckLandLogic.Player import Player
from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from DuckLandLogic.Message.Chat.GlobalChatLineMessage import GlobalChatLineMessage


class SendGlobalChatLineMessage(PiranhaMessage):
    def __init__ (self):
        super().__init__(0)
        self.message = ""
        
    def decode(self):
        super().decode()
        self.message = self.stream.readString()

    def getMessage(self):
        return self.message

    def setMessage(self, message: str):
        self.message = message

    def getMessageType(self):
        return 14715