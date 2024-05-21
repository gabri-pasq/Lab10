from dataclasses import dataclass

@dataclass
class Confine:
    numero: int
    stato1: int
    stato2: int

    def __hash__(self):
        return hash(self.numero)

    def __str__(self):
        return f'{self.stato1} - {self.stato2}'