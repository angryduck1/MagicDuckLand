from DuckLandTitan.Logic.DataStream.ByteStream import ByteStream

class PiranhaMessage:
    def __init__(self, messageVersion) -> None:
        self.stream = ByteStream(10) #ByteStream = this + 8
        self.messageVersion = messageVersion #this + 1
    
    def clear(self, capacity):
        return self.stream.clear(capacity)

    def encode(self):
        pass

    def decode(self):
        pass

    def isClientToServerMessage(self):
        return self.getMessageType - 10000 < 10000 #getMessageType = this + 20
    
    def isServerToClientMessage(self):
        return self.getMessageType - 20000 < 10000
    
    def getByteStream(self):
        return self.stream
    
    def getMessageBytes(self):
        return self.stream.getByteArray()
    
    def getEncodingLength(self):
        return self.stream.getLength()
    
    def getMessageType(self) -> int:
        return 0
    
    def getMessageVersion(self):
        return self.messageVersion
    
    def setMessageVersion(self, messageVersion):
        self.messageVersion = messageVersion

    def destruct(self):
        self.stream.destruct()