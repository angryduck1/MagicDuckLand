from DuckLandTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from DuckLandTitan.Logic.Math.LogicLong import LogicLong

class LoginMessage(PiranhaMessage):
    def __init__(self) -> None:
        super().__init__(0)
        self.AccountId: LogicLong = LogicLong()
        self.AndroidID = " " #this + 144
        self.ClientMajorVersion = -1 #this + 14
        self.ClientBuild = -1 #this + 15
        self.PrefferedLanguage = 0 #this + 27
        self.isAndroid = 0 #this + 168
        self.passToken = self.stream.readString()

    def getAndroidID(self):
        return self.AndroidID
    
    def getClientMajorVersion(self):
        return self.ClientMajorVersion
    
    def getClientBuild(self):
        return self.ClientBuild
    
    def getPreferredLanguage(self):
        return self.PrefferedLanguage
    
    def isAndroid(self):
        return self.isAndroid
    
    def getMessageType(self) -> int:
        return 10101
    
    def decode(self):
        super().decode()
        self.accountId = self.stream.readLong()
        self.passtoken = self.stream.readString()
        self.ClientMajorVersion = self.stream.readInt()
        self.stream.readInt()
        self.ClientBuild = self.stream.readInt()
        self.ResourceSha = self.stream.readString()
        self.UDID = self.stream.readString()
        self.OpenUDID = self.stream.readString()
        self.MacAddress = self.stream.readString()