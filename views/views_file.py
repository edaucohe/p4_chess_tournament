from typing import Dict  # , List
from dataclasses import dataclass, asdict  # , field

from models.models_file import Player, Points, Score


@dataclass
class InfoPlayers:
    info_players = {}  # : Dict = field(init=False)
    players_list = []  # : List = field(init=False)
    players_points = 0
    players_score = 0

    # def __post_init__(self):
    #     self.info_players = {}
    #     self.players_list = []

    def get_players_info(self) -> Dict:
        print("Merci de taper les coordonnées des joueurs : ")
        self.info_players = asdict(Player(input("Prénom : "),
                                          input("Nom : "),
                                          input("Date de naissance : "),
                                          input("Sexe : "),
                                          int(input("Classement : "))
                                          )
                                   )

        return self.info_players

    def get_players_points(self):
        self.players_points = Points.points
        return self.players_points

    def get_players_score(self):
        self.players_score = Score(float(input("Points : ")))
        return self.players_score

    def show_players(self, players_list):
        self.players_list = players_list
        print("---- Info des joueurs (dans le view) ----")
        print(self.players_list)
