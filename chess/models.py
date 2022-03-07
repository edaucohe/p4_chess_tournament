from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Tuple, Dict
from dataclasses import dataclass, field

DEFAULT_PLAYERS_NUMBER = 8
DEFAULT_TURNS_COUNT = 4
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


class PlayerScore:
    player_score: Tuple[Player, Optional[MatchResult]] = (Player, field(default=SCORE_INIT))


# Match = Tuple[List[Player, Optional[MatchResult]], List[Player, Optional[MatchResult]]]
# Match = Tuple[List[Union[Player, Optional[MatchResult]]], List[Union[Player, Optional[MatchResult]]]]
class Match:
    match: Tuple[Tuple[PlayerScore], Tuple[PlayerScore]]


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
    turn_count: int = DEFAULT_TURNS_COUNT
    round: List[Round] = field(default_factory=lambda: [])


class MainMenu(Enum):
    TOURNAMENT_MANAGEMENT = 1
    PLAYERS_MANAGEMENT = 2
    MAKE_REPORTS = 3
    SAVE_DATA = 4
    CLOSE_APPLI = 5


class PlayerManagementMenu(Enum):
    PLAYERS_LIST = 1
    ENTER_NEW_PLAYER = 2
    PLAYER_DATA_UPDATE = 3
    PREVIOUS_MENU = 4


class TournamentManagementMenu(Enum):
    TOURNAMENTS_LIST = 1
    MAKE_NEW_TOURNAMENT = 2
    START_TOURNAMENT = 3
    TOURNAMENT_DATA_UPDATE = 4
    PREVIOUS_MENU = 5


class MakeNewTournamentMenu(Enum):
    PLAYERS_FROM_DATA_BASE = 1
    PLAYERS_FROM_TYPING = 2
    PREVIOUS_MENU = 3


class SaveData(Enum):
    SAVE_DATA = 1
    LOAD_DATA = 2
    PREVIOUS_MENU = 3


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
    UPDATE_PLAYER_INFO = 1
    PREVIOUS_MENU = 2


class ReportMenu(Enum):
    PLAYERS_REPORT = 1
    PLAYERS_TOURNAMENT_REPORT = 2
    TOURNAMENTS_REPORT = 3
    ROUNDS_REPORT = 4
    MATCHS_REPORT = 5
    PREVIOUS_MENU = 6


# @dataclass
# class MainMenu:
#     1: "Créer un tournoi"
#     2: "Modifier les coordonnées d'un tournoi",
#     3: "Initier un tournoi",
#     4: "Ajouter un joueur",
#     5 : "Mettre à jour les coordonnées d'un joueur",
#     6: "Créer un rapport",
#     7: "Fermer l'application"
