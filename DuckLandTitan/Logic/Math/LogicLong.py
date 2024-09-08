class LogicLong:
    def __init__(self, highInteger: int = 0, lowInteger: int = 0) -> None:
        self.highInteger = highInteger #this
        self.lowInteger = lowInteger #this + 1

    def decode(self, stream) -> None:
        self.highInteger = stream.readInt()
        self.lowInteger = stream.readInt()

    def encode(self, encoder) -> None:
        encoder.writeInt(self.highInteger)
        encoder.writeInt(self.lowInteger)
    
    def __str__(self) -> str:
        return f"{self.highInteger}-{self.lowInteger}"