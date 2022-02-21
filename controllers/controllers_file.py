from typing import List, Dict
from dataclasses import dataclass

from views.views_file import InfoPlayers

PLAYERS_NUMBER = 2


@dataclass
class Controller:
    players_to_add = InfoPlayers()
    list_players = []

    def add_players(self) -> List[Dict]:
        for players_number in range(PLAYERS_NUMBER):
            player_added = self.players_to_add.get_players_info()
            self.list_players.append(player_added)

        return self.list_players

    def sent_players_to_screen(self):
        self.players_to_add.show_players(self.list_players)
