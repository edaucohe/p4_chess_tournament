from typing import List, Dict
from dataclasses import dataclass

from views.views_file import InfoPlayers

PLAYERS_NUMBER = 5


@dataclass
class Controller:
    players_to_add = InfoPlayers()
    list_players = []
    players_ranking_order = []

    def add_players(self) -> List[Dict]:
        for players_number in range(PLAYERS_NUMBER):
            player_added = self.players_to_add.get_players_info()
            self.list_players.append(player_added)

        return self.list_players

    def send_players_to_screen(self):
        self.players_to_add.show_players(self.list_players)

    def classify_players(self):
        """Classification par la méthode de tri à bulles - ordre descendant"""
        for iteration_one in range(len(self.list_players)-1):
            print("Valeur de player_number ONE : ", iteration_one)
            for iteration_two in range(len(self.list_players) - 1):
                print("Valeur de player_number TWO : ", iteration_two)
                if self.list_players[iteration_two+1]["ranking"] > self.list_players[iteration_two]["ranking"]:
                    self.list_players[iteration_two+1], self.list_players[iteration_two] = \
                        self.list_players[iteration_two], self.list_players[iteration_two+1]
                    self.players_ranking_order = self.list_players
                    print("Valeur de players_ranking : ", self.players_ranking_order)
