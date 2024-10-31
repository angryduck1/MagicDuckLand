from DuckLandTitan.Logic.Message import PiranhaMessage
from DuckLandServer.Protocol.Messaging import Messaging

from DuckLandLogic.Message.Home.OwnHomeDataMessage import OwnHomeDataMessage
from DuckLandLogic.Message.Account.LoginMessage import LoginMessage
from DuckLandLogic.Message.Account.LoginOkMessage import LoginOkMessage
from DuckLandLogic.Message.Alliance.SearchAlliancesMessage import SearchAlliancesMessage
from DuckLandLogic.Message.Alliance.AllianceListMessage import AllianceListMessage
from DuckLandLogic.Message.Profile.AskForAvatarProfileMessage import AskForAvatarProfileMessage
from DuckLandLogic.Message.Profile.AvatarProfileMessage import AvatarProfileMessage
from DuckLandLogic.Message.Alliance.CreateAlliance.CreateAllianceMessage import CreateAllianceMessage
from DuckLandLogic.Message.Alliance.CreateAlliance.AllianceCreateFailedMessage import *
from DuckLandLogic.Message.Chat.SendGlobalChatLineMessage import SendGlobalChatLineMessage
from DuckLandLogic.Message.Chat.GlobalChatLineMessage import GlobalChatLineMessage
from DuckLandLogic.Message.LeaderBoard.AskForAvatarRankingListMessage import AskForAvatarRankingListMessage
from DuckLandLogic.Message.LeaderBoard.AvatarRankingListMessage import AvatarRankingListMessage
from DuckLandLogic.Message.Battles.AttackNpcMessage import AttackNpcMessage
from DuckLandLogic.Message.Battles.NpcDataMessage import NpcDataMessage

class MessageManager:
    def __init__(self, messaging: Messaging) -> None:
        self.messaging = messaging
    
    def receiveMessage(self, message: PiranhaMessage):
        messageType = message.getMessageType()

        if messageType == 10101:
            self.onLoginMessage(self, message)
        elif messageType == 14102:
            pass
        elif messageType == 14324:
            self.messaging.sendMessage(AllianceListMessage())
        elif messageType == 14325:
            self.messaging.sendMessage(AvatarProfileMessage())
        elif messageType == 14301:
            self.messaging.sendMessage(AllianceCreateFailedMessage())
        elif messageType == 14715:
            self.onSendGlobalChatMessage(message)
        elif messageType == 14403:
            self.messaging.sendMessage(AvatarRankingListMessage())
        elif messageType == 14134:
            self.messaging.sendMessage(NpcDataMessage())
        else:
            print("Unknown message type: " + str(messageType))
    def __str__(self) -> str:
        return f"{self.highInteger}-{self.lowInteger}"

    def onLoginMessage(self, message, loginMessage: LoginMessage):
        print(f"[MessageManager] Logged in! AccountId: {loginMessage.accountId.__str__()} PassToken: {loginMessage.passToken} ClientMajorVersion: {loginMessage.ClientMajorVersion} ClientBuild: {loginMessage.ClientBuild} ResourceSha: {loginMessage.ResourceSha}")

        self.messaging.sendMessage(LoginOkMessage())
        self.messaging.sendMessage(OwnHomeDataMessage())


        if isinstance(message, LoginMessage):
            
            print("Login message received")
        else:
            print("Received message of wrong type for onLoginMessage")

    def onSendGlobalChatMessage(self, sendGlobalChatLineMessage: SendGlobalChatLineMessage):
        print(f"New message: {sendGlobalChatLineMessage.getMessage()}")

        globalChatLineMessage = GlobalChatLineMessage()
        globalChatLineMessage.setMessage(sendGlobalChatLineMessage.getMessage())
        self.messaging.sendMessage(globalChatLineMessage)