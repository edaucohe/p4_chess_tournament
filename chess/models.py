from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Tuple
from dataclasses import dataclass, field

DEFAULT_PLAYERS_NUMBER = 2
DEFAULT_TURNS_COUNT = 4
MENU_OPTION = ""


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


# Match = Tuple[List[Player, Optional[MatchResult]], List[Player, Optional[MatchResult]]]
class Match:
    match: Tuple[List[Player, Optional[MatchResult]], List[Player, Optional[MatchResult]]]


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
    BULLET = 'bullet'
    BLITZ = 'blitz'
    QUICK_PLAY = 'quick_play'


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


class MainMenu(Enum):
    MAKE_TOURNAMENT = 1
    MODIFY_TOURNAMENT = 2
    START_TOURNAMENT = 3
    ADD_PLAYERS = 4
    UPDATE_PLAYERS = 5
    MAKE_REPORT = 6
    CLOSE_APPLI = 7


class NewTournamentMenu(Enum):
    ENTER_NEW_TOURNAMENT = 1
    PREVIOUS_MENU = 2


class ModifyTournamentMenu(Enum):
    MODIFY_TOURNAMENT = 1
    PREVIOUS_MENU = 2


class StartTournamentMenu(Enum):
    START_TOURNAMENT = 1
    PREVIOUS_MENU = 2


class NewPlayerMenu(Enum):
    ENTER_NEW_PLAYER = 1
    PREVIOUS_MENU = 2


class ModifyPlayerInfoMenu(Enum):
    MODIFY_PLAYER_INFO = 1
    PREVIOUS_MENU = 2


class ReportMenu(Enum):
    PLAYERS_LIST = 1
    PLAYERS_TOURNAMENT_LIST = 2
    TOURNAMENT_LIST = 3
    ROUNDS_LIST = 4
    MATCHS_LIST = 5
    PREVIOUS_MENU = 6


# @dataclass
# class MainMenu:
#     1: "Créer un tournoi"
#     2: "Modifier les coordonnées d'un tournoi",
#     3: "Initier un tournoi",
#     4: "Ajouter un joueur",
#     5: "Mettre à jour les coordonnées d'un joueur",
#     6: "Créer un rapport",
#     7: "Fermer l'application"
