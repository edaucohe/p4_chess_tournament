from collections import Counter
from typing import List, Dict
from dataclasses import dataclass

from views.views_file import InfoPlayers
from models.models_file import Points

PLAYERS_NUMBER = 4


@dataclass
class Controller:
    players_to_add = InfoPlayers()
    points = Points()
    list_players = []
    players_ranking_order = []
    players_points = []
    list_starting_points = []
    groups = {}
    number_of_groups = 0

    def add_players(self) -> (List[Dict], List):
        """Joueurs ajoutés + points de départ égal à 0 """
        for players_number in range(PLAYERS_NUMBER):
            player_added = self.players_to_add.get_players_info()
            # self.list_players.append(player_added)
            # starting_points = self.points.points
            starting_points = self.players_to_add.get_players_score().score  # Code pour remplir le score
            self.list_starting_points.append(starting_points)
            print("starting points : ", self.list_starting_points)
            self.list_players.append((player_added, starting_points))

        groupes = self.groups_number(self.list_starting_points)
        print("nb. de groupes : ", groupes)

        return self.list_players

    def send_players_to_screen(self):
        self.players_to_add.show_players(self.list_players)

    def classify_by_ranking(self):
        """Classification par la méthode de tri à bulles - ordre descendant"""
        for iteration_one in range(len(self.list_players)-1):
            for iteration_two in range(len(self.list_players) - 1):
                if self.list_players[iteration_two+1][0]["ranking"] > self.list_players[iteration_two][0]["ranking"]:
                    self.list_players[iteration_two+1], self.list_players[iteration_two] = \
                        self.list_players[iteration_two], self.list_players[iteration_two+1]
                    self.players_ranking_order = self.list_players
                    print("Valeur de players_ranking : ", self.players_ranking_order)

    def groups_number(self, list_points):
        self.groups = Counter(list_points)
        for group in range(len(self.groups)):
            self.number_of_groups += 1

        return self.number_of_groups

    def classify_by_points(self):
        # """Classification par la méthode de tri à bulles - ordre descendant des Points"""
        #
        # for iteration_one in range(len(self.list_players)-1):
        #     for iteration_two in range(len(self.list_players) - 1):
        #         if self.list_players[iteration_two+1]["ranking"] > self.list_players[iteration_two]["ranking"]:
        #             self.list_players[iteration_two+1], self.list_players[iteration_two] = \
        #                 self.list_players[iteration_two], self.list_players[iteration_two+1]
        #             self.players_ranking_order = self.list_players
        #             print("Valeur de players_ranking : ", self.players_ranking_order)
        pass

    # def assign_points(self):
    #     for players_number in range(PLAYERS_NUMBER):
    #         player = self.list_players[players_number]
    #         points = self.points.points
    #         self.players_points.append((player, points))
    #     print("Tuple des joueurs avec leurs points : ", self.players_points)

    def define_matchs(self):

        pass
