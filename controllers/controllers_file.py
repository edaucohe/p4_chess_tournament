from typing import List, Dict
from dataclasses import dataclass

from views.views_file import InfoPlayers
# from models.models_file import Player


@dataclass
class Controller:
    players_to_add = InfoPlayers()
    list_players = []

    def add_players(self) -> List[Dict]:
        for nb in range(2):
            player_added = self.players_to_add.get_players_info()
            self.list_players.append(player_added)

        return self.list_players


@dataclass
class Test:
    z: int = 0

    def somme(self, x, y):
        self.z = x + y
        return self.z
