from DuckLandTitan.Logic.Message import PiranhaMessage
from DuckLandServer.Protocol.Messaging import Messaging

from DuckLandLogic.Message.Home.OwnHomeDataMessage import OwnHomeDataMessage
from DuckLandLogic.Message.Account.LoginMessage import LoginMessage
from DuckLandLogic.Message.Account.LoginOkMessage import LoginOkMessage

class MessageManager:
    def __init__(self, messaging: Messaging) -> None:
        self.messaging = messaging

    def receiveMessage(self, message: PiranhaMessage):
        messageType = message.getMessageType()

        if messageType == 10101:
            self.onLoginMessage(self, message)
        elif messageType == 14102:
            pass
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