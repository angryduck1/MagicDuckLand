from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from DuckLandLogic.Player import Player
from DuckLandLogic.Message.Alliance.CreateAlliance.AllianceCreateFailedMessage import *

class CreateAllianceMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)
    
    def decode(self):

        self.stream.readString()  
        self.stream.readString()

        self.stream.readInt()

        self.stream.readInt()
        self.stream.readInt()

    def getMessageType(self):
        return 14301