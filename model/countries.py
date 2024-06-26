from dataclasses import dataclass

@dataclass
class Country:
    cCode: int
    stateAbb: str
    stateNme: str

    def __hash__(self):
        return hash(self.cCode)

    def __str__(self):
        return f'{self.stateAbb}'