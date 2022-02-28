from collections import Counter
from typing import List, Dict, Optional
from dataclasses import dataclass

from chess.views import TerminalView
from chess.models import Player, Tournament, DEFAULT_PLAYERS_NUMBER


# @dataclass
# class State:
#     players: List[Player]
#     tournaments: List[Tournament]
#     current_tournament: Optional[Tournament]
#
#
# class Controller:
#     def __init__(self, state: Optional[State] = None, view: Optional[TerminalView] = None):
#         self.state = state or State
#         self.view = view or TerminalView()


class Controller:
    def __init__(
            self,
            players: Optional[List[Player]] = None,
            tournaments: Optional[List[Tournament]] = None,
            current_tournament: Optional[List[Tournament]] = None,
            view: Optional[TerminalView] = None
    ):
        self.players = players or Player
        self.tournaments = tournaments or Tournament
        self.current_tournament = current_tournament or Tournament
        self.view = view or TerminalView()

    # def __add__(self, other):

    def display_main_menu(self):
        n = self.view.display_main_menu()
        if n == "add_players":
            print("valeur de n (add player) egal a : ", n)
            self.add_players()

    def add_players(self) -> (List[Dict], List):
        """Joueurs ajoutés + points de départ égal à 0 """
        self.player_list = []
        for players_number in range(DEFAULT_PLAYERS_NUMBER):
            player = self.view.enter_new_player()
            self.player_list.append(player)
            print("Valeur de player : ", self.player_list)
            # self.players.append(player)

            # player_added = self.players_to_add.get_players_info()
            # # self.list_players.append(player_added)
            # # starting_points = self.points.points
            # starting_points = self.players_to_add.get_players_score().score  # Code pour remplir le score
            # self.list_starting_points.append(starting_points)
            # print("starting points : ", self.list_starting_points)
            # self.list_players.append((player_added, starting_points))

        # groupes = self.groups_number(self.list_starting_points)
        # print("nb. de groupes : ", groupes)

        return self.players

    def print_all_players(self):
        self.view.print_players_report(self.state.players)

    def print_tournament_players(self):
        self.view.print_players_report(self.state.current_tournament.players)

    def classify_by_ranking(self):
        # Tri croissant
        # p1 rank=1 en premier, p2 rank=2 en 2e
        sorted_players_by_ranking = sorted(self.state.players, key=lambda p: p.ranking)

        # Tri décroissant
        # p1 score=5000 en premier, p2 score=4000 en deuxième
        sorted_players_by_points = sorted(self.state.players, key=lambda p: p.points, reverse=True)

        """Classification par la méthode de tri à bulles - ordre descendant"""
        for iteration_one in range(len(self.list_players) - 1):
            for iteration_two in range(len(self.list_players) - 1):
                if self.list_players[iteration_two + 1][0]["ranking"] > self.list_players[iteration_two][0]["ranking"]:
                    self.list_players[iteration_two + 1], self.list_players[iteration_two] = \
                        self.list_players[iteration_two], self.list_players[iteration_two + 1]
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
