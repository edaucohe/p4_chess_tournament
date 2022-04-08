import dataclasses
from datetime import date, datetime
from enum import Enum
from typing import Any, List, Optional, Tuple, Dict, Union
from dataclasses import dataclass, field

DEFAULT_PLAYERS_NUMBER = 8
MAX_TURNS_COUNT = 4
DEFAULT_TURN_COUNT = 4
TEST_TURN_COUNT = 2
SCORE_INIT = 0
MENU_OPTION = ""
DEFAULT_ROUND_VALUE = []
NUMBER_MAX_OF_HEADS = 5

JsonDict = Dict[str, Any]


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

    def update_player(self, first_name, last_name, date_of_birth, sex, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.ranking = ranking

    def to_json(self) -> Dict[str, Any]:
        # Serialization
        player_as_dict = dataclasses.asdict(self)
        player_as_dict['date_of_birth'] = self.date_of_birth.isoformat()
        player_as_dict['sex'] = self.sex.value
        return player_as_dict

    @classmethod
    def from_json(cls, data: JsonDict) -> 'Player':
        # Deserialization
        data['date_of_birth'] = date.fromisoformat(data['date_of_birth'])
        data['sex'] = Sex(data['sex'])
        return Player(**data)


class MatchResult(Enum):
    WIN = 1
    LOSS = 0
    DRAW = 0.5


Match = Tuple[List[Union[Player, Optional[MatchResult]]], List[Union[Player, Optional[MatchResult]]]]


@dataclass
class Round:
    matches: List[Match]
    name: str
    start: datetime = field(default_factory=datetime.now)
    end: Optional[datetime] = None

    def close(self):
        self.end = datetime.now()

    def to_json(self):
        # Serialization
        round_as_json = dataclasses.asdict(self)
        round_as_json['start'] = self.start.isoformat()
        round_as_json['end'] = None if self.end is None else self.end.isoformat()

        # Serialize matches
        for match_number, match in enumerate(self.matches):
            for player_number, player in enumerate(match):
                round_as_json['matches'][match_number][player_number][0] = player[0].to_json()
                round_as_json['matches'][match_number][player_number][1] = \
                    None if not isinstance(player[1], MatchResult) else player[1].value

        return round_as_json

    @classmethod
    def from_json(cls, data: JsonDict):
        # Deserialization
        data['start'] = datetime.fromisoformat(data['start'])
        data['end'] = None if data['end'] is None else datetime.fromisoformat(data['end'])

        # Deserialize matches
        for match_number, match in enumerate(data['matches']):
            for player_number, player in enumerate(match):
                data['matches'][match_number][player_number][0] = \
                    Player.from_json(data['matches'][match_number][player_number][0])
                data['matches'][match_number][player_number][1] = \
                    MatchResult(player[1]) if isinstance(player[1], int) or isinstance(player[1], float) else 0

        return Round(**data)


class TimeControlKind(Enum):
    BULLET = 'bullet'
    BLITZ = 'blitz'
    QUICK_PLAY = 'quick play'


@dataclass
class Tournament:
    name: str
    place: str
    time_control: TimeControlKind
    description: str
    players: Dict[int, Player]
    scores: Dict[int, float]
    start: Optional[date] = None
    round_count: int = DEFAULT_TURN_COUNT
    rounds: List[Round] = field(default_factory=lambda: [])

    def current_round(self):
        return self.rounds[-1]

    def init(self):
        self.generate_scores()
        self.generate_next_round()
        self.start = date.today()

    def generate_scores(self):
        for player_id in self.players.keys():
            self.scores[player_id] = 0

    def generate_next_round(self):
        players_sorted = self.sort_players()
        if not self.rounds:
            matches = self.generate_matches_for_first_round(players_sorted)
        else:
            matches = self.generate_matches_for_other_rounds(players_sorted)

        next_round = Round(matches=matches, name="ROUND " + str(len(self.rounds) + 1))
        self.rounds.append(next_round)

    def sort_players(self):
        players_to_sort = {}
        for player_id, player in self.players.items():
            players_to_sort[player] = self.scores[player_id]

        return sorted(players_to_sort.items(), key=lambda scores: (scores[1], scores[0].ranking), reverse=True)

    @staticmethod
    def generate_matches_for_first_round(players_sorted):
        matches = []
        for number_of_match in range(len(players_sorted) - 4):
            matches.append((list(players_sorted[number_of_match]), list(players_sorted[number_of_match + 4])))
        return matches

    @staticmethod
    def generate_matches_for_other_rounds(players_sorted):
        matches = []
        for number_of_match in range(len(players_sorted) - 4):
            matches.append((list(players_sorted[number_of_match * 2]), list(players_sorted[number_of_match * 2 + 1])))
        return matches

    def enter_match_result(self, match_selected, result_selected):
        for match in self.rounds[-1].matches:
            if match == match_selected:
                message = ""
                if result_selected == 1:
                    message = f"{match[0][0].first_name} {match[0][0].last_name} a gagné le match !"
                    for player_id, player in self.players.items():
                        if match[0][0] == player:
                            self.scores[player_id] += 1
                    match[0][1] = MatchResult.WIN
                    match[1][1] = MatchResult.LOSS
                elif result_selected == 2:
                    message = f"{match[1][0].first_name} {match[1][0].last_name} a gagné le match !"
                    for player_id, player in self.players.items():
                        if match[1][0] == player:
                            self.scores[player_id] += 1
                    match[0][1] = MatchResult.LOSS
                    match[1][1] = MatchResult.WIN
                elif result_selected == 3:
                    message = "Les joueurs ont fait match null"
                    for player_id, player in self.players.items():
                        if match[0][0] == player:
                            self.scores[player_id] += 0.5
                        if match[1][0] == player:
                            self.scores[player_id] += 0.5
                    match[0][1] = MatchResult.DRAW
                    match[1][1] = MatchResult.DRAW
                return message

    def update_tournament(self, name, place, time_control, description):
        self.name = name
        self.place = place
        self.time_control = time_control
        self.description = description

    def to_json(self):
        # Serialization
        tournament_as_dict = dataclasses.asdict(self)
        tournament_as_dict['time_control'] = self.time_control.value
        tournament_as_dict['start'] = None if self.start is None else self.start.isoformat()

        # Serialize players
        for player_id, player in tournament_as_dict['players'].items():
            tournament_as_dict['players'][player_id]['date_of_birth'] = player['date_of_birth'].isoformat()
            tournament_as_dict['players'][player_id]['sex'] = player['sex'].value

        # Serialize rounds
        tournament_as_dict['rounds'] = [current_round.to_json() for current_round in self.rounds]

        return tournament_as_dict

    @classmethod
    def from_json(cls, data: JsonDict):
        data['start'] = None if data['start'] is None else date.fromisoformat(data['start'])
        data['time_control'] = TimeControlKind(data['time_control'])

        # Deserialize players
        data['players'] = {player_id: Player.from_json(player) for player_id, player in data['players'].items()}

        # Deserialize rounds
        data['rounds'] = [Round.from_json(current_round) for current_round in data['rounds']]

        return Tournament(**data)
