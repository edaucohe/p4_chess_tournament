from dataclasses import dataclass
from models.models_file import Player


@dataclass
class InfoPlayers:

    def get_players_info(self):
        print("Merci de taper les coordonnées des joueurs : ")
        self.info_players = Player(first_name=input("Prénom : "),
                                   last_name=input("Nom : "),
                                   day_of_birth=input("Date de naissance : "),
                                   sex=input("Sexe : "),
                                   ranking =input("Classement : ")
                                   )

        return self.info_players
