from typing import Dict
from dataclasses import dataclass, asdict

from models.models_file import Player
# from controllers.controllers_file import Controller


@dataclass
class InfoPlayers:
    info_players: Dict = ""

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
