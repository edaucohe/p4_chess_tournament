from typing import List, Dict
from dataclasses import dataclass, field


@dataclass
class Player:
    first_name: str
    last_name: str
    day_of_birth: str
    sex: str
    ranking: int


@dataclass
class Tournament:
    tournament_name: str
    place: str
    date: str
    turn: int = field(init=False)
    round: List
    players: List
    match_time: int
    description: str

    def __post_init__(self):
        self.turn = 4


@dataclass
class Round:
    round_name: str
    match: List
    start_date: str
    start_hour: int
    end_date: str
    end_hour: int


@dataclass
class Match:
    players: Dict
    score: int


@dataclass
class Points:
    points: int = field(init=False)

    def __post_init__(self):
        self.points = 0


@dataclass
class Score:
    score: float
