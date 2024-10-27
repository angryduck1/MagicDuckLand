from DuckLandTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from DuckLandTitan.Logic.Math.LogicLong import LogicLong
from DuckLandLogic.Base.LogicBase import LogicBase
import json
from pathlib import Path

class LogicClientHome(LogicBase):
    def __init__(self) -> None:
        super().__init__()
        filepath = Path(__file__).parent / 'data.json'
        with open(filepath, 'r') as file:
            self.HomeJSON = json.load(file)
        self.jsonString = json.dumps(self.HomeJSON)
        self.ChangeListener = 0
        self.getId = 0
        self.ShieldDurationSeconds = 0
        self.DefenseRating = 0
        self.DefenseRating = 0
    
    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeLong(LogicLong(1, 1)) #id
        encoder.writeString(self.jsonString)
        encoder.writeInt(0) # ShieldDurationSeconds
        encoder.writeInt(0)  #DefenseRating
        encoder.writeInt(0) # DefenseKFactor