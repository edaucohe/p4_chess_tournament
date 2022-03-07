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
            players: Optional[Dict[int, List]] = None,
            tournaments: Optional[List[Tournament]] = None,
            current_tournament: Optional[List[Tournament]] = None,
            view: Optional[TerminalView] = None,
    ):
        self.players = players or dict()
        self.tournaments = tournaments or []
        self.current_tournament = current_tournament or None
        self.view = view or TerminalView()
        # self.players_in_tournament = dict()
        # self.player_score = player_score or PlayerScore
        # self.tournament_selected = []

    # def __add__(self, other):

    def display_menus(self):
        option_selected = self.view.display_main_menu()
        return option_selected

    def display_players_list(self):
        self.view.display_players_list(self.players)

    def enter_new_player(self, index):  # -> (List[Dict], List):
        """Joueurs ajoutés + points de départ égal à 0 """
        player = self.view.enter_new_player()
        self.players.update({index: player})

    def update_player_info(self):
        print("print de self.players : ", self.players)
        print("type de self.players : ", type(self.players))
        self.players = self.view.update_player_info(self.players)

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

    def display_tournaments_list(self):
        print("Tournois : ", self.tournaments)
        self.view.display_tournaments_list(self.tournaments)

    def make_new_tournament(self, option_selected):
        players_id = []
        players_id_set = {}
        players_in_tournament = {}
        option_selected = option_selected
        number_of_players = len(self.players)
        if option_selected == "PLAYERS_FROM_DATA_BASE":
            print("option_selected : ", option_selected)
            self.display_players_list()
            print(f"\nChoisissez {DEFAULT_PLAYERS_NUMBER} joueurs")

            for player_number in range(DEFAULT_PLAYERS_NUMBER):
                player_id = self.view.enter_new_players_in_tournament(
                    player_number+1, number_of_players, players_id_set)
                players_id.append(player_id)
                players_id_set = set(players_id)
                players_in_tournament.update({player_id: self.players.get(player_id)})
                print("self.players_in_tournament : ", players_in_tournament)

        elif option_selected == "PLAYERS_FROM_TYPING":
            print("option_selected : ", option_selected)
            # for player_number in range(DEFAULT_PLAYERS_NUMBER):
            #     self.view.enter_new_player()

        tournament = self.view.enter_new_tournament(players_in_tournament)
        print("Tournoi créé : ", tournament)
        self.tournaments.append(tournament)

        # self.display_make_new_tournament_menu()
        # tournament = self.view.enter_new_tournament(self.tournaments)
        # print("Tournoi créé : ", tournament)
        # self.tournaments.append(tournament)
        # return self.tournaments

    def display_make_new_tournament_menu(self):
        score = MatchResult
        players_with_score = []
        players_source = self.view.display_make_new_tournament_menu()
        if players_source == "PLAYERS_FROM_DATA_BASE":
            self.display_players_list()
        elif players_source == "PLAYERS_FROM_DATA_BASE":
            for player_number in range(DEFAULT_PLAYERS_NUMBER):
                player = self.enter_new_player()
                players_with_score.append([player, score.LOSS])
                self.players


    def modify_tournament(self):
        # self.view.display_modify_tournament_menu()
        self.view.display_tournaments_list(self.tournaments)
        # pass

    def start_tournament(self):
        # self.tournament_selected = self.view.display_tournaments_list(self.tournaments)
        print("tournoi choisi : ", self.tournament_selected)
        # round = self.tournament_selected[ROUND_NUMBER_POSITION]
        # print("valeur de round : ", round)
        players_ordered_by_score = self.classify_by_score(self.tournament_selected)
        print("en ordre selon points : ", players_ordered_by_score)
        players_ordered_by_ranking = self.classify_by_ranking(players_ordered_by_score)
        print("en ordre selon classement : ", players_ordered_by_ranking)

    def make_players_report(self):
        self.view.make_players_report(self.players)

    def run_chess_script(self):
        run = True
        while run:
            option_selected = self.display_menus()
            if option_selected == "ENTER_NEW_PLAYER":
                print("valeur de l'option selected : ", option_selected)
                index = len(self.players) + 1
                self.enter_new_player(index)
                print("liste de joueurs avec identifiant", self.players)
                # self.classify_by_points()
                # self.classify_by_ranking()
            elif option_selected == "PLAYERS_LIST":
                print("valeur de l'option selected : ", option_selected)
                self.display_players_list()
                run = True
            elif option_selected == "PLAYER_DATA_UPDATE":
                print("valeur de l'option selected : ", option_selected)
                self.update_player_info()
                run = True
            elif option_selected == "TOURNAMENTS_LIST":
                self.display_tournaments_list()
                # print("Tournois : ", self.tournaments)
                run = True
            elif option_selected == "PLAYERS_FROM_DATA_BASE":
                self.make_new_tournament(option_selected)
                # print("Tournois : ", self.tournaments)
                run = True
            elif option_selected == "PLAYERS_FROM_TYPING":
                self.make_new_tournament(option_selected)
                # print("Tournois : ", self.tournaments)
                run = True
            elif option_selected == "modify_tournament":
                self.modify_tournament()
                run = True
            elif option_selected == "start_tournament":
                self.start_tournament()
                run = True
            elif option_selected == "PLAYERS_REPORT":
                self.make_players_report()
                # print("Tournois : ", self.tournaments)
                run = True
            elif option_selected == "close_script":
                run = False
