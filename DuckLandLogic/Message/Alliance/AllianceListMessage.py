from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage

class AllianceListMessage(PiranhaMessage):

    def __init__(self):
        super().__init__(0)
        self.id = 24310

    def encode(self):

        self.stream.writeString("value")

        self.stream.writeInt(1)

    def getMessageType(self):
        return 24310