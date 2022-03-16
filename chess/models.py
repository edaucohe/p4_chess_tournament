import dataclasses
from datetime import date, datetime
from enum import Enum
from typing import Any, List, Optional, Tuple, Dict, Union
from dataclasses import dataclass, field

DEFAULT_PLAYERS_NUMBER = 8
MAX_TURNS_COUNT = 4
DEFAULT_TURN_COUNT = 1
TEST_TURN_COUNT = 2
SCORE_INIT = 0
MENU_OPTION = ""
DEFAULT_ROUND_VALUE = []
NUMBER_MAX_OF_HEADS = 5


class Sex(Enum):
    MALE = 'h'
    FEMALE = 'f'


@dataclass(unsafe_hash=True)
class Player:
    first_name: str
    last_name: str
    date_of_birth: date
    sex: Sex
    ranking: int

    def to_json(self) -> Dict[str, Any]:
        # Serialization
        player_as_dict = dataclasses.asdict(self)
        player_as_dict['date_of_birth'] = self.date_of_birth.isoformat()
        player_as_dict['sex'] = self.sex.value
        return player_as_dict

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> 'Player':
        # Deserialization
        data['date_of_birth'] = date.fromisoformat(data['date_of_birth'])
        data['sex'] = Sex(data['sex'])

        return Player(**data)

# p1 => p1_as_dict => p1_as_dict_as_json
# Pour la db, on veut passer de :
# player = Player('name', 'lastname', date.today(), Sex.FEMALE, 1)
# à
# player = {'first_name': 'name', 'last_name': 'lastname', 'date_of_birth': '2022-03-16', 'sex': 'f', 'ranking': 1}


class MatchResult(Enum):
    WIN = 1
    LOSS = 0
    DRAW = 0.5


Match = Tuple[List[Union[Player, Optional[MatchResult]]], List[Union[Player, Optional[MatchResult]]]]
# OR
# Match = Tuple[Tuple[Player, Optional[MatchResult]], Tuple[Player, Optional[MatchResult]]]


@dataclass
class Round:
    # un match = ((player1, win), (player2, loss))  OU si le match n'est pas joué (player1, None), (player2, None)
    # 1er round, matches = [match(p1, p5), match(p2, p6), match(p3, p7), match(p4, p8)]
    # players -> reorder with their score
    # 2e round, matches = [match(p1, p2), match(p3, p4), match(p5, p6), match(p7, p8)]
    matches: List[Match]
    name: str
    start: datetime = field(default_factory=datetime.now)

    '''Champ Date et heure de fin'''
    end: Optional[datetime] = None

    '''Qui doit être automatiquement rempli lorsque l'utilisateur le marque comme terminé'''

    def close(self):
        self.end = datetime.now()


class TimeControlKind(Enum):
    BULLET = 'bullet'
    BLITZ = 'blitz'
    QUICK_PLAY = 'quick play'


class OrderPlayerList(Enum):
    ALPHABETICAL = 'a'
    RANKING = 'c'


@dataclass
class Tournament:
    name: str
    place: str
    time_control: TimeControlKind
    description: str
    players: Dict[int, Player]  # {1: Player1}
    scores: Dict[Player, float]  # {Player1: 3.5}
    start: date = field(default_factory=date.today)
    round_count: int = DEFAULT_TURN_COUNT

    # rounds = [round1, round2, ...]
    # current round = rounds[-1]
    # max(len(rounds)) = turn_count
    rounds: List[Round] = field(default_factory=lambda: [])
