from datetime import date
from typing import Any, Callable, Dict, List  # , List
from dataclasses import dataclass, asdict  # , field

from chess.models import Player, Sex


# @dataclass
# class InfoPlayers:
#     info_players = {}  # : Dict = field(init=False)
#     players_list = []  # : List = field(init=False)
#     players_points = 0
#     players_score = 0
#
#     # def __post_init__(self):
#     #     self.info_players = {}
#     #     self.players_list = []
#
#     def get_players_info(self) -> Dict:
#         print("Merci de taper les coordonnées des joueurs : ")
#         self.info_players = asdict(
#             Player(
#                 input("Prénom : "),
#                 input("Nom : "),
#                 input("Date de naissance : "),
#                 input("Sexe : "),
#                 int(input("Classement : "))
#             )
#         )
#
#         return self.info_players
#
#     def get_players_points(self):
#         self.players_points = Points.points
#         return self.players_points
#
#     def get_players_score(self):
#         self.players_score = Score(float(input("Points : ")))
#         return self.players_score
#
#     def show_players(self, players_list):
#         self.players_list = players_list
#         print("---- Info des joueurs (dans le view) ----")
#         print(self.players_list)


def input_with_constraint(desc: str, parse_fn: Callable[[str], Any]):
    while True:
        try:
            input_value = input(desc)
            return parse_fn(input_value)
        except:
            # print error message?
            pass


def parse_positive_int(input_as_str: str) -> int:
    value: int = int(input_as_str)
    assert value > 0
    return value


class TerminalView:
    def enter_new_player(self) -> Player:
        # How to parse/validate?
        player = Player(
            first_name=input('First name: '),
            last_name=input('Last name: '),
            date_of_birth=input_with_constraint('DoB: ', parse_fn=date.fromisoformat),
            sex=input_with_constraint('Genre (m/f): ', parse_fn=Sex),
            ranking=input_with_constraint('Ranking (must be >0): ', parse_fn=parse_positive_int)
        )

        return player

    def display_players(self, players: List[Player]):
        for idx, player in enumerate(players):
            print(f'{idx} -- {player}')

    def format_players_json(self, players: List[Player]) -> str:
        json_str = "["
        for player in players:
            json_str += player.as_json()
            json_str += ","
        json_str += "]"
        return json_str

    def print_players_report(self, players: List[Player]):
        # in controller.print_all_players():
        #     self.view.print_players_report(self.players)

        # in controller.print_tournament_players():
        #     self.view.print_players_report(self.current_tournament.players)
        pass


