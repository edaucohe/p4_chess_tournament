from datetime import date, datetime
from enum import Enum
from typing import Any, List, Dict, Optional, Tuple
from dataclasses import dataclass, field

DEFAULT_TURNS_COUNT = 4

DEFAULT_PLAYERS_NUMBER = 4


class Sex(Enum):
    Male = 'm'
    Female = 'f'


@dataclass
class Player:
    first_name: str
    last_name: str
    date_of_birth: date
    sex: Sex
    ranking: int


class MatchResult(Enum):
    Win = 1
    Loss = 0
    Draw = 0.5


Match = Tuple[Tuple[Player, Optional[MatchResult]], Tuple[Player, Optional[MatchResult]]]


# Elle doit également contenir un champ Date et heure de fin,
@dataclass
class Round:
    matches: List[Match]
    name: str

    start: datetime = field(default_factory=datetime.now)

    # Elle doit également contenir un champ Date et heure de fin,
    end: Optional[datetime] = None

    def close(self):
        # qui doit être automatiquement rempli lorsque l'utilisateur le marque comme terminé
        self.end = datetime.now()


class TimeControlKind(Enum):
    Bullet = 'bullet'
    Blitz = 'blitz'
    QuickPlay = 'quick_play'


@dataclass
class Tournament:
    name: str
    place: str
    start: date
    time_control: TimeControlKind
    players: List[Player]
    round: List[Round]
    description: str
    turn_count: int = DEFAULT_TURNS_COUNT

