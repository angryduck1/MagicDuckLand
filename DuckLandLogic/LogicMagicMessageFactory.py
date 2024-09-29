from DuckLandLogic.Message.Account.LoginMessage import LoginMessage
from DuckLandServer.Protocol.EndClientTurnMessage import EndClientTurnMessage
from DuckLandLogic.Message.Alliance.SearchAlliancesMessage import SearchAlliancesMessage
from DuckLandLogic.Message.Profile.AskForAvatarProfileMessage import AskForAvatarProfileMessage
from DuckLandLogic.Message.Alliance.CreateAlliance.CreateAllianceMessage import CreateAllianceMessage

class LogicMagicMessageFactory:
    messages = {
        10101: LoginMessage,
        14102: EndClientTurnMessage,
        14324: SearchAlliancesMessage,
        14325: AskForAvatarProfileMessage,
        14301: CreateAllianceMessage
    }

    @staticmethod
    def createMessageByType(messageType, data=None, device=None):
        messages = LogicMagicMessageFactory.messages
        if messageType in messages.keys():
            message_class = messages[messageType]
            if message_class is not None:
                print("[LogicMagicMessageFactory]", str(messageType) + " created")
                return message_class(data, device) if messageType == 14324 else message_class()
        return None