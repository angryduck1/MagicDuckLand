from DuckLandLogic.Player import Player
from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from DuckLandLogic.Message.Chat.GlobalChatLineMessage import GlobalChatLineMessage


class SendGlobalChatLineMessage(PiranhaMessage):
    def __init__ (self):
        super().__init__(0)

    def decode(self):

        self.stream.readString()

    def getMessageType(self):
        return 14715