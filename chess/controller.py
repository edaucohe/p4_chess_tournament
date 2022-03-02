from collections import Counter
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

from chess.views import TerminalView
from chess.models import Player, Tournament, DEFAULT_PLAYERS_NUMBER, PlayerScore, MatchResult


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
            players: Optional[Dict[int, Player]] = None,
            tournaments: Optional[List[Tournament]] = None,
            current_tournament: Optional[List[Tournament]] = None,
            view: Optional[TerminalView] = None,
    ):
        self.players = players or dict()
        self.tournaments = tournaments or []
        self.current_tournament = current_tournament or None
        self.view = view or TerminalView()
        # self.player_score = player_score or PlayerScore
        # self.tournament_selected = []

    # def __add__(self, other):

    def display_menus(self):
        option_selected = self.view.display_main_menu()
        return option_selected

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

        # return self.players

    def print_all_players(self):
        self.view.print_players_report(self.state.players)

    def print_tournament_players(self):
        self.view.print_players_report(self.state.current_tournament.players)

    def classify_by_ranking(self, players_list):
        sorted_players_by_ranking = sorted(players_list, key=lambda r: r[0].ranking, reverse=True)
        return sorted_players_by_ranking

    def groups_number(self, list_points):
        self.groups = Counter(list_points)
        for group in range(len(self.groups)):
            self.number_of_groups += 1

        return self.number_of_groups

    def classify_by_score(self, tournament_selected):
        sorted_players_by_score = sorted(tournament_selected.players, key=lambda score: score[1], reverse=True)
        return sorted_players_by_score

    # def assign_points(self):
    #     for players_number in range(PLAYERS_NUMBER):
    #         player = self.list_players[players_number]
    #         points = self.points.points
    #         self.players_points.append((player, points))
    #     print("Tuple des joueurs avec leurs points : ", self.players_points)

    def define_matchs(self):
        pass

    def make_tournament(self):
        tournament = self.view.enter_new_tournament()
        print("Valeur du tournoi : ", tournament)
        self.tournaments.append(tournament)
        return self.tournaments

    def modify_tournament(self):
        # self.view.display_modify_tournament_menu()
        self.view.display_tournaments_list(self.tournaments)
        # pass

    def start_tournament(self):
        self.tournament_selected = self.view.display_tournaments_list(self.tournaments)
        print("tournoi choisi : ", self.tournament_selected)
        # round = self.tournament_selected[ROUND_NUMBER_POSITION]
        # print("valeur de round : ", round)
        players_ordered_by_score = self.classify_by_score(self.tournament_selected)
        print("en ordre selon points : ", players_ordered_by_score)
        players_ordered_by_ranking = self.classify_by_ranking(players_ordered_by_score)
        print("en ordre selon classement : ", players_ordered_by_ranking)

    def run_chess_script(self):
        run = True
        while run:
            option_selected = self.display_menus()
            if option_selected == "add_players":
                print("valeur de l'option selected : ", option_selected)
                self.add_players()
                # self.classify_by_points()
                self.classify_by_ranking()
            elif option_selected == "make_tournament":
                self.tournaments = self.make_tournament()
                print("Tournois : ", self.tournaments)
                run = True
            elif option_selected == "modify_tournament":
                self.modify_tournament()
                run = True
            elif option_selected == "start_tournament":
                self.start_tournament()
                run = True
            elif option_selected == "close_script":
                run = False
