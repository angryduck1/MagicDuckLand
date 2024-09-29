from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage

class AllianceCreateFailedMessage(PiranhaMessage):

    def __init__(self):
        super().__init__(0)
        self.id = 24332

    def encode(self):
        self.stream.writeInt(1)

    def getMessageType(self):
        return 24332