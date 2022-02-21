from typing import Dict  # , List
from dataclasses import dataclass, asdict  # , field

from models.models_file import Player


@dataclass
class InfoPlayers:
    info_players = {}  # : Dict = field(init=False)
    players_list = []  # : List = field(init=False)

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

    def show_players(self, players_list):
        self.players_list = players_list
        print("---- Info des joueurs (dans le view) ----")
        print(self.players_list)
