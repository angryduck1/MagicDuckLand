from DuckLandTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from DuckLandTitan.Logic.Math.LogicLong import LogicLong
from DuckLandLogic.Base.LogicBase import LogicBase

class LogicClientAvatar(LogicBase):
    def __init__(self) -> None:
        super().__init__()

        self.resources = {
            3000001: 8888888, #Gold
            3000002: 7777777, #Elixir
        }
        self.Diamonds = 999999

        self.tutorialSteps = list(range(21000000, 21000013)) # tutor steps

    def encode(self, encoder: ChecksumEncoder):
        encoder.writeInt(0) #LogicDataVersion
        encoder.writeInt(0) #HighID
        encoder.writeInt(1) #LowID
        encoder.writeInt(0) #HighAllianceId
        encoder.writeInt(1) #LowAllianceId

        encoder.writeBoolean(False)

        encoder.writeInt(0) #LeagueType
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeString("angryduck001") #getName
        encoder.writeString("") #getFacebookId
        encoder.writeInt(10) #ExpLevel
        encoder.writeInt(999) #ExpPoints
        encoder.writeInt(self.Diamonds) #Diamods
        encoder.writeInt(0) #FreeDiamonds
        encoder.writeInt(0) #AttackRating
        encoder.writeInt(0) #AttackKFactor
        encoder.writeInt(9999) #Score
        encoder.writeInt(0) #AttackWinCount
        encoder.writeInt(0) #LoseCount
        encoder.writeInt(0) #DefenseWinCount
        encoder.writeInt(0) #DefenseLoseCount
        encoder.writeBoolean(False) #setNameSetByUser
        encoder.writeInt(0) #CumulativePurchasedDiamonds

        encoder.writeInt(0) #SetResources
        encoder.writeInt(len(self.resources))

        for resource_id, value in self.resources.items():
            encoder.writeInt(resource_id)
            encoder.writeInt(value)

        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)