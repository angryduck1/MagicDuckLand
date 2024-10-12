class LogicLong:
    def __init__(self, highInteger: int = 0, lowInteger: int = 0):
        self.highInteger = highInteger #this
        self.lowInteger = lowInteger #this + 1

    def decode(self, stream):
        self.highInteger = stream.readInt()
        self.lowInteger = stream.readInt()

    def encode(self, encoder):
        encoder.writeInt(self.highInteger)
        encoder.writeInt(self.lowInteger)
    
    def __str__(self) -> str:
        return f"{self.highInteger}-{self.lowInteger}"
