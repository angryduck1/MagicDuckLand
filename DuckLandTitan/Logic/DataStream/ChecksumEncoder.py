from DuckLandTitan.Logic.Math.LogicLong import LogicLong

class ChecksumEncoder:
    def __init__(self) -> None:
        self.checksum = 0 #this +2, this +8
        self.snapshotCheckusm = 0 #this +3, this + 12, 0xC
        self.enabled = True #this +4
 
    def destruct(self):
        self.checksum = 0
        self.snapshotCheckusm = 0
        self.enabled = True

    def enableCheckSum(self,enable):
        if not self.enabled or enable:
            if not self.enabled and enable == True:
                self.checksum = self.snapshotChecksum
                self.enabled = enable
        else:
            self.snapshotCheckusm = self.checksum
            self.enabled = False

    def getCheckSum(self):
        return self.checksum
    
    def isCheckSumEnabled(self):
        return self.enabled
    
    def isCheckSumOnlyMode(self):
        return True
    
    def resetCheckSum(self):
        self.checksum = 0

    def writeBoolean(self, value: bool):
        if value == True:
            self.checksum + 13
        else:
            self.checksum + 7
        self.checksum + self.rotateRight(self.checksum, 31)

    def writeByte(self, value):
        self.checksum = value + self.rotateRight(self.checksum, 31) + 11

    def writeBytes(self, value: bytes, length: int):
        if value is not None:
            self.checksum = length + 28
        else:
            self.checksum = 27
        self.checksum = self.checksum + self.rotateRight(self.checksum, 31)

    def writeInt(self, value: int):
        self.checksum = value + self.rotateRight(self.checksum, 31) + 9

    def writeLong(self, value: LogicLong):
        value.encode(self)

    def writeString(self, value: str):
        if value is not None:
            self.checksum = len(value) + 28
        else:
            self.checksum = 27
        self.checksum + self.rotateRight(self.checksum, 31)
        
    def writeStringReference(self, value):
        self.checksum = len(value) + self.rotateRight(self.checksum, 31) + 38

    @staticmethod
    def rotateRight(value: int, count: int):
        return (value >> count) | (value << (32 - count))