from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Tuple, Dict, Union
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


@dataclass
class Player:
    first_name: str
    last_name: str
    date_of_birth: date
    sex: Sex
    ranking: int


class MatchResult(Enum):
    WIN = 1
    LOSS = 0
    DRAW = 0.5


# class PlayerScore:
#     player_score: Tuple[Player, Optional[MatchResult]] = (Player, field(default=SCORE_INIT))


# Match = Tuple[List[Player, Optional[MatchResult]], List[Player, Optional[MatchResult]]]
# match: Tuple[Tuple[Player, Optional[MatchResult]], Tuple[Player, Optional[MatchResult]]]
# Match = Tuple[List[Union[Player, Optional[MatchResult]]], List[Union[Player, Optional[MatchResult]]]]
# match: Tuple[Tuple[PlayerScore], Tuple[PlayerScore]]
# match = Tuple[List[Union[Player, Optional[MatchResult]]], List[Union[Player, Optional[MatchResult]]]]
# class PlayerResult:
#     player_result: Tuple[Player, Optional[MatchResult]]


@dataclass
class Match:
    # player_one_result: Tuple[Player, Optional[MatchResult]]
    # player_two_result: Tuple[Player, Optional[MatchResult]]
    # result: []
    match: Tuple[List[Union[Player, Optional[MatchResult]]], List[Union[Player, Optional[MatchResult]]]]

    # def result(self):
    #     return list[self.player_one_result, self.player_two_result]
    # return self.result

    # def player_one_wins(self):
    #     pass
    #
    # def player_two_wins(self):
    #     pass
    #
    # def draw(self):
    #     pass


@dataclass
class Round:
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
    players: Dict[int, List]
    start: date = field(default_factory=date.today)
    turn_count: int = DEFAULT_TURN_COUNT
    round: List[Round] = field(default_factory=lambda: [])
