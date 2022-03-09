from collections import Counter
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, fields

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

    def classify_players_by_name_report(self, players_list):
        players_sorted_by_name = sorted(players_list.items(), key=lambda n: n[1][0].last_name)
        return players_sorted_by_name

    def classify_players_by_ranking_report(self, players_list):
        players_sorted_by_name = sorted(players_list.items(), key=lambda n: n[1][0].ranking, reverse=True)
        return players_sorted_by_name

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
        # self.view.enter_tournament_selection(self.tournaments)

    def make_new_tournament(self, option_selected):
        players_id = []
        players_id_set = {}
        players_in_tournament = {}
        number_of_players = len(self.players)
        if option_selected == "PLAYERS_FROM_DATA_BASE":
            print("option_selected : ", option_selected)
            self.display_players_list()
            print(f"\nChoisissez {DEFAULT_PLAYERS_NUMBER} joueurs")

            for player_number in range(DEFAULT_PLAYERS_NUMBER):
                player_id = self.view.enter_new_players_in_tournament(
                    player_number + 1, number_of_players, players_id_set)
                players_id.append(player_id)
                players_id_set = set(players_id)
                players_in_tournament.update({player_id: self.players.get(player_id)})
                print("self.players_in_tournament : ", players_in_tournament)

        elif option_selected == "PLAYERS_FROM_TYPING":
            print("option_selected : ", option_selected)
            # for player_number in range(DEFAULT_PLAYERS_NUMBER):
            #     self.view.enter_new_player()

        tournament = self.view.enter_new_tournament()
        tournament.players = players_in_tournament

        print("Tournoi créé : ", tournament)
        self.tournaments.append(tournament)

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

    def make_players_alphabetical_report(self, players, report, tournament_name):
        row_lists = []
        # report = "alphabetical"
        players_by_alphabetical_order = self.classify_players_by_name_report(players)
        print("self.players : ", players)
        print("players_by_alphabetical_order : ", players_by_alphabetical_order)

        for index, player in players_by_alphabetical_order:
            player_info = player[0]
            row_list = [index,
                        player_info.first_name,
                        player_info.last_name,
                        player_info.date_of_birth,
                        player_info.sex,
                        player_info.ranking
                        ]
            print("row_list : ", row_list)
            row_lists.append(row_list)

        file_name = str(tournament_name) + " (joueurs par ordre alphabetique)"
        self.view.make_players_report(row_lists, report, file_name)

    def make_players_ranking_report(self, players, report, tournament_name):
        row_lists = []
        # report = "ranking"
        players_by_ranking_order = self.classify_players_by_ranking_report(players)
        print("self.players : ", players)
        print("players_by_alphabetical_order : ", players_by_ranking_order)

        for index, player in players_by_ranking_order:
            player_info = player[0]
            row_list = [index,
                        player_info.first_name,
                        player_info.last_name,
                        player_info.date_of_birth,
                        player_info.sex,
                        player_info.ranking
                        ]
            print("row_list : ", row_list)
            row_lists.append(row_list)

        file_name = str(tournament_name) + " (joueurs par classement)"
        self.view.make_players_report(row_lists, report, file_name)

    def make_players_alphabetical_by_tournament_report(self):
        self.display_tournaments_list()

    def make_players_ranking_by_tournament_report(self):
        pass

    def make_players_by_tournament_report(self):
        # self.display_tournaments_list()
        tournament = self.view.enter_tournament_selection(self.tournaments)
        print("tournament : ", tournament)
        players = tournament.players
        print("players : ", players)
        selection = self.view.display_players_by_tournament_menu()
        if selection == "ALPHABETICAL_BY_TOURNAMENT":
            tournament_name = str(tournament.name)
            report = "players_in_tournament_by_alphabetical_order"
            self.make_players_alphabetical_report(players, report, tournament_name)
        elif selection == "RANKING_BY_TOURNAMENT":
            tournament_name = str(tournament.name)
            report = "players_in_tournament_by_ranking_order"
            self.make_players_ranking_report(players, report, tournament_name)

    def tournaments_management_menu(self):
        choices = {
            1: "Choice 1",
            2: "Go Back"
        }

        name = "Tournament Management"
        run = True
        while run:
            user_choice = self.view.display_menu_with_input(name, choices)
            if user_choice == 1:
                print('Choice 1')
            elif user_choice == 2:
                run = False

    def players_management_menu(self):
        choices = {
            1: "Choice 1",
            2: "Go Back"
        }
        name = "Players"
        run = True
        while run:
            user_choice = self.view.display_menu_with_input(name, choices)
            if user_choice == 1:
                user = self.view.enter_new_player()
                # do stuff with user
            elif user_choice == 2:
                run = False

    def reports_menu(self):
        choices = {
            1: "Players report",
            2: "Current tournament players report",
            3: "Go Back"
        }
        reports_to_display = {
            1: self.make_players_alphabetical_report,
            2: self.make_players_alphabetical_by_tournament_report,
        }
        name = "Reports"
        run = True
        while run:
            user_choice = self.view.display_menu_with_input(name, choices)
            if user_choice == 3:
                run = False
            else:
                reports_to_display[user_choice]()

    def data_management_menu(self):
        choices = {
            1: "Choice 1",
            2: "Go Back"
        }
        name = "Database"
        run = True
        while run:
            user_choice = self.view.display_menu_with_input(name, choices)
            if user_choice == 1:
                print('Choice 1')
            elif user_choice == 2:
                run = False

    def main_menu(self):
        choices_names = {
            1: "Gestion de tournois",
            2: "Gestion de joueurs",
            3: "Création de rapports",
            4: "Sauvegarder/Charger les données",
            5: "Fermer l'application"
        }
        choices_actions = {
            1: self.tournaments_management_menu,
            2: self.players_management_menu,
            3: self.reports_menu,
            4: self.data_management_menu,
        }
        name = "Main menu"
        run = True
        while run:
            user_choice = self.view.display_menu_with_input(name, choices_names)
            if user_choice == 5:
                self.view.display_close_message()
                run = False
            else:
                choices_actions[user_choice]()

