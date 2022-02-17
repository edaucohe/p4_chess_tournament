from dataclasses import dataclass


@dataclass
class Player:
    first_name: str
    last_name: str
    day_of_birth: str
    sex: str
    ranking: int
