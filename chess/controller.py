from collections import Counter
from typing import List, Dict, Optional

from chess.views import TerminalView
from chess.models import Player, Tournament, DEFAULT_PLAYERS_NUMBER, Round, Match, MatchResult


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
            tournaments: Optional[Dict[int, Tournament]] = None,
            current_tournament: Optional[Tournament] = None,
            view: Optional[TerminalView] = None,
            round_info: Optional[Round] = None,
            # match: Optional[Match] = None
    ):
        self.players = players or dict()
        self.tournaments = tournaments or dict()
        self.current_tournament = current_tournament or None
        self.view = view or TerminalView()
        self.round = round_info or None
        self.all_matches = []
        # self.match_result = match or []
        # self.player_one_result = match.player_one_result or ()
        # self.player_two_result = match.player_two_result or ()
        # self.match = match or ()

        # self.players_in_tournament = dict()
        # self.player_score = player_score or PlayerScore
        # self.tournament_selected = []

    @staticmethod
    # def clear_screen():
    #     # os.system('cls')
    #     if os.name == 'nt':
    #         os.system('cls')
    #     else:
    #         print("\n"*10)
    #     return 0

    # def __add__(self, other):

    def display_menus(self):
        option_selected = self.view.display_main_menu()
        return option_selected

    # def display_players_list(self):
    #     self.view.display_players_list(self.players)

    # def enter_player_info(self):  # -> (List[Dict], List):
    #     player = self.view.enter_player_info()
    #     return player

    # def update_player_info(self):
    #     print("print de self.players : ", self.players)
    #     print("type de self.players : ", type(self.players))
    #     self.players = self.view.update_player_info(self.players)

    # def print_all_players(self):
    #     self.view.print_players_report(self.state.players)
    #
    # def print_tournament_players(self):
    #     self.view.print_players_report(self.state.current_tournament.players)

    def classify_by_ranking(self, players_list):
        sorted_players_by_ranking = sorted(players_list, key=lambda r: r[0].ranking, reverse=True)
        return sorted_players_by_ranking

    def groups_number(self, list_points):
        groups = Counter(list_points)
        for group in range(len(groups)):
            self.number_of_groups += 1

        return self.number_of_groups

    @staticmethod
    def classify_by_score(tournament_selected):
        sorted_players_by_score = sorted(tournament_selected.players, key=lambda score: score[1], reverse=True)
        return sorted_players_by_score

    @staticmethod
    def classify_players_by_name_report(players_list):
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

    # def display_tournaments_list(self):
    #     print("Tournois : ", self.tournaments)
    #     self.view.display_tournaments_list(self.tournaments)
        # self.view.enter_tournament_selection(self.tournaments)

    # def make_new_tournament(self, option_selected):
    #     players_id = []
    #     players_id_set = {}
    #     players_in_tournament = {}
    #     number_of_players = len(self.players)
    #     if option_selected == "PLAYERS_FROM_DATA_BASE":
    #         print("option_selected : ", option_selected)
    #         self.display_players_list()
    #         print(f"\nChoisissez {DEFAULT_PLAYERS_NUMBER} joueurs")
    #
    #         for player_number in range(DEFAULT_PLAYERS_NUMBER):
    #             player_id = self.view.enter_new_players_in_tournament(
    #                 player_number + 1,
    #                 number_of_players,
    #                 players_id_set
    #             )
    #             players_id.append(player_id)
    #             players_id_set = set(players_id)
    #             players_in_tournament.update({player_id: self.players.get(player_id)})
    #             print("self.players_in_tournament : ", players_in_tournament)
    #
    #     elif option_selected == "PLAYERS_FROM_TYPING":
    #         print("option_selected : ", option_selected)
    #         # for player_number in range(DEFAULT_PLAYERS_NUMBER):
    #         #     self.view.enter_new_player()
    #
    #     tournament = self.view.enter_new_tournament()
    #     tournament.players = players_in_tournament
    #
    #     print("Tournoi créé : ", tournament)
    #     self.tournaments.append(tournament)

    # def display_make_new_tournament_menu(self):
    #     score = MatchResult
    #     players_with_score = []
    #     players_source = self.view.display_make_new_tournament_menu()
    #     if players_source == "PLAYERS_FROM_DATA_BASE":
    #         self.display_players_list()
    #     elif players_source == "PLAYERS_FROM_DATA_BASE":
    #         for player_number in range(DEFAULT_PLAYERS_NUMBER):
    #             player = self.enter_new_player()
    #             players_with_score.append([player, score.LOSS])
    #             self.players

    def modify_tournament(self):
        # self.view.display_modify_tournament_menu()
        self.view.display_tournaments_list(self.tournaments)
        # pass

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
        # self.display_tournaments_list()
        pass

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

    '''Script que je travaille'''
    def enter_new_player_info(self):
        id_new_player = len(self.players) + 1
        new_player = self.view.enter_player_info()
        self.players.update({id_new_player: new_player})

    def update_player_info(self):
        choices = self.display_players_list()
        player_id_selected = self.view.input_for_menu(choices)
        player = self.view.enter_player_info()
        self.players.update({player_id_selected: player})

    def make_new_tournament(self):
        players_id__selected_list = []
        players_in_current_tournament = {}
        choices = self.display_players_list()

        id_new_tournament = len(self.tournaments) + 1
        new_tournament = self.view.enter_tournament_info(players_in_current_tournament)
        self.tournaments.update({id_new_tournament: new_tournament})

        for player_number in range(DEFAULT_PLAYERS_NUMBER):
            player_id_selected = self.view.input_for_menu(choices)
            while player_id_selected in players_id__selected_list:
                print("choisissez un autre joueur !")
                player_id_selected = self.view.input_for_menu(choices)

            player = self.players[player_id_selected]
            players_in_current_tournament.update({player_id_selected: player})
            players_id__selected_list.append(player_id_selected)

        new_tournament.players = players_in_current_tournament
        print("new_tournament : ", new_tournament)
        print("self.tournaments : ", self.tournaments)

    def update_tournament_info(self):
        choices = self.display_tournament_list()
        tournament_id_selected = self.view.input_for_menu(choices)
        players_in_current_tournament = self.tournaments.get(tournament_id_selected).players
        tournament = self.view.enter_tournament_info(players_in_current_tournament)
        self.tournaments.update({tournament_id_selected: tournament})

    def current_round(self):
        pass

    def enter_round_info(self, end_date):
        round_info = self.view.enter_round_info(end_date=end_date)
        return round_info

    # @staticmethod
    # def current_round_number(current_tournament):
    #     if current_tournament.turn_count == 1:
    #         print(current_tournament.round.__getattribute__("name"))
    #     elif current_tournament.turn_count == 2:
    #         print("deuxième tour")
    #     elif current_tournament.turn_count == 3:
    #         print("troisième tour")
    #     elif current_tournament.turn_count == 4:
    #         print("dernier tour")

    def tournament_management_round_one(self, players_in_groups):
        print("tournament_management_round_one")

    @staticmethod
    def make_list_of_matches(players_in_group):
        matches = []
        matches_by_group = []
        for player_in_group in players_in_group:
            print("player_in_group : ", player_in_group)
            matches.append(player_in_group)
            if len(matches) == 2:
                matches_by_group.append(matches)
                matches = []
        return matches_by_group

    def matches_by_round_management(self, players_in_groups):
        all_matches = []
        next_group_of_players = 1
        for players_in_group in players_in_groups:
            print("Nb de joueurs du groupe : ", len(players_in_group))
            if len(players_in_group) % 2 == 0:
                '''Nb pair de joueurs -> opposer les joueurs par ordre descendant'''
                print("Nb PAIR de joueurs")
                matches_by_group = self.make_list_of_matches(players_in_group)
                all_matches.extend(matches_by_group)
            else:
                '''Nb impair de joueurs -> placer le dernier joueur dans le groupe suivant'''
                print("Nb IMPAIR de joueurs")
                last_player = players_in_group.pop()
                print("last_player", last_player)
                players_in_groups[next_group_of_players].insert(0, last_player)
                print("players_in_group[next_group_of_players] : ", players_in_groups[next_group_of_players])
                matches_by_group = self.make_list_of_matches(players_in_group)
                all_matches.extend(matches_by_group)

            next_group_of_players += 1

        return all_matches

    @staticmethod
    def groups_formed_by_frequency_of_scores(players_with_score: List[List]) -> Dict:
        score_values = []
        for player_with_score in players_with_score:
            score_values.append(player_with_score[1])

        groups = Counter(score_values)
        sorted_groups = sorted(groups.items(), key=lambda item: item[0], reverse=True)
        return dict(sorted_groups)

    @staticmethod
    def order_players_by_score(players_with_score: List[List]) -> List[List]:
        sorted_players_by_score = sorted(players_with_score, key=lambda score: score[1], reverse=True)
        return sorted_players_by_score

    @staticmethod
    def order_players_by_ranking(players_ordered_by_score: List[List]) -> List[List]:
        sorted_players_by_ranking = sorted(players_ordered_by_score, key=lambda r: r[0].ranking, reverse=True)
        return sorted_players_by_ranking

    def classify_players_in_groups(self, players_with_score: List[List]) -> List[List[List]]:
        index_of_player = 0
        list_of_groups = []

        groups_generated_by_counting_score = self.groups_formed_by_frequency_of_scores(players_with_score)
        players_ordered_by_score = self.order_players_by_score(players_with_score)

        '''Formation de groupes + tri par classement'''
        for score, number_of_players in groups_generated_by_counting_score.items():
            group = []
            for number_of_player in range(number_of_players):
                group.append(players_ordered_by_score[index_of_player+number_of_player])

            group_of_players_ordered_by_ranking = self.order_players_by_ranking(group)
            print("players_group_ordered_by_ranking : ", group_of_players_ordered_by_ranking)

            index_of_player += number_of_players
            list_of_groups.append(group_of_players_ordered_by_ranking)

        return list_of_groups

    def start_tournament(self):
        self.all_matches = []
        players_with_score = []
        # all_matches = []
        n = 0
        score = 0

        # TODO Code pour générer des scores pour les joueurs
        for player_id, player in self.current_tournament.players.items():
            players_with_score.append([player, score])
            if n % 3 == 0:
                score = 1
            elif n % 3 == 1:
                score = 0
            else:
                score = 0.5
            n += 1
        # TODO jusqu'ici

        players_in_groups = self.classify_players_in_groups(players_with_score)
        print("players_in_groups : ", players_in_groups)

        print(f"-- {self.current_tournament.round.__getattribute__('name')} --")
        if self.current_tournament.turn_count == 1:
            self.tournament_management_round_one(players_in_groups)
        else:
            self.all_matches = self.matches_by_round_management(players_in_groups)

        print("all_matches = ", self.all_matches)

        '''Voulez-vous entrer les résultats d un match ?'''
        self.display_matches_list_menu()
        # print("list_of_matches : ", list_of_matches)
        # print("new_all_matches : ", new_all_matches)

        # current_round = self.enter_round_info()

        # if round_number == 1:
        #     pass

    def evaluate_current_tournament_status(self, tournament_id_selected):
        self.current_tournament = []
        self.current_tournament = self.tournaments.get(tournament_id_selected)
        print("current_tournament : ", self.current_tournament)
        round_in_current_tournament = self.tournaments.get(tournament_id_selected).round
        end_value_of_current_round = round_in_current_tournament.__getattribute__('end')

        if end_value_of_current_round is None:
            message = f"\n** {self.current_tournament.name} **"
            self.view.display_a_simple_message(message)
            self.start_tournament()
        else:
            message = "\n** Tournoi déjà fini =( **"
            self.view.display_a_simple_message(message)

    # def player_one_wins(self, all_matches, match_selection, name_of_player):
    #     match_result = MatchResult
    #     message = f"{name_of_player} a gagné le match"
    #     self.view.display_a_simple_message(message)
    #
    #     player_one_result = [all_matches[match_selection-1][0][0], match_result.WIN]
    #     player_two_result = [all_matches[match_selection-1][1][0], match_result.LOSS]
    #     print("all_matches[match_selection-1][0][0] type : ", type(all_matches[match_selection-1][0][0]))
    #
    #     print("Match : ", Match((player_one_result, player_two_result)))
    #
    # def player_two_wins(self, all_matches, match_selection, name_of_player):
    #     match_result = MatchResult
    #     message = f"{name_of_player} a gagné le match"
    #     self.view.display_a_simple_message(message)
    #
    #     player_one_result = [all_matches[match_selection-1][0][0], match_result.LOSS]
    #     player_two_result = [all_matches[match_selection-1][1][0], match_result.WIN]
    #     print("match_result : ", Match((player_one_result, player_two_result)))
    #
    # def draw(self, all_matches, match_selection):
    #     match_result = MatchResult
    #     message = "Les joueurs ont fait un match nul"
    #     self.view.display_a_simple_message(message)
    #
    #     player_one_result = [all_matches[match_selection-1][0][0], match_result.DRAW]
    #     player_two_result = [all_matches[match_selection-1][1][0], match_result.DRAW]
    #     print("match_result : ", Match((player_one_result, player_two_result)))

    def enter_match_result(self, player_one, player_two, match_selection):
        match_result = MatchResult
        list_of_matches = self.current_tournament.round.__getattribute__("matches")
        # list_of_rounds = [self.current_tournament.round]
        # print("list_of_rounds : ", list_of_rounds)

        if match_selection == 1:
            message = f"{player_one[0].first_name + ' ' + player_one[0].last_name} a gagné le match"
            self.view.display_a_simple_message(message)
            match = Match(([player_one[0], match_result.WIN], [player_two[0], match_result.LOSS]))
            list_of_matches.append(match)
            # list_of_rounds.append(self.current_tournament.round)
            self.current_tournament.round = \
                Round(name=self.current_tournament.round.__getattribute__("name"), matches=list_of_matches)
        elif match_selection == 2:
            message = f"{player_two[0].first_name + ' ' + player_two[0].last_name} a gagné le match"
            self.view.display_a_simple_message(message)
            match = Match(([player_one[0], match_result.LOSS], [player_two[0], match_result.WIN]))
            list_of_matches.append(match)
            # list_of_rounds.append(self.current_tournament.round)
            self.current_tournament.round = \
                Round(name=self.current_tournament.round.__getattribute__("name"), matches=list_of_matches)
        elif match_selection == 3:
            message = "Les joueurs ont fait un match nul"
            self.view.display_a_simple_message(message)
            match = Match(([player_one[0], match_result.DRAW], [player_two[0], match_result.DRAW]))
            list_of_matches.append(match)
            # list_of_rounds.append(self.current_tournament.round)
            self.current_tournament.round = \
                Round(name=self.current_tournament.round.__getattribute__("name"), matches=list_of_matches)
        print("list_of_matches : ", list_of_matches)

    def enter_match_result_menu(self, match_selection):
        player_one = self.all_matches[match_selection-1][0]
        player_two = self.all_matches[match_selection-1][1]
        choices = {
            1: player_one[0].first_name + " " + player_one[0].last_name,
            2: player_two[0].first_name + " " + player_two[0].last_name,
            3: "Match null",
            4: "Revenir au menu précédent"
        }

        name = " Qui a gagné le match ? "
        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == 4:
                run = False
            else:
                self.enter_match_result(player_one, player_two, user_choice)
                print("self.current_tournament : ", self.current_tournament)
                run = False

            # return match
                # all_matches[match_selection - 1][0][1] = p1_new_score
                # all_matches[match_selection - 1][1][1] = p2_new_score
                # return match, all_matches

    '''Generation de listes à afficher'''
    @staticmethod
    def generate_tournaments_list(tournaments):
        choices = {}
        for tournament_number in range(len(tournaments)):
            choices.update({tournament_number + 1: tournaments.get(tournament_number + 1).name})
        name = " Liste de tournois "
        return name, choices

    def display_tournament_list(self):
        name, choices = self.generate_tournaments_list(self.tournaments)
        self.view.display_menu(name, choices)
        return choices

    @staticmethod
    def generate_players_list(players):
        choices = {}
        for player_number in range(len(players)):
            choices.update({
                player_number + 1:
                    players.get(player_number + 1).first_name + " " + players.get(player_number + 1).last_name
            })
        name = " Liste de joueurs "
        return name, choices

    def display_players_list(self):
        name, choices = self.generate_players_list(self.players)
        self.view.display_menu(name, choices)
        return choices

    @staticmethod
    def generate_matches_list(all_matches_list):
        choices = {}
        for match_number in range(len(all_matches_list)):
            choices.update({
                match_number + 1:
                    all_matches_list[match_number][0][0].first_name + " " +
                    all_matches_list[match_number][0][0].last_name +
                    " vs " +
                    all_matches_list[match_number][1][0].first_name + " " +
                    all_matches_list[match_number][1][0].last_name})
        name = " Liste de matches "
        return name, choices

    @staticmethod
    def generate_players_report_list(players):
        choices = {}
        for player_number in range(len(players)):
            choices.update({
                player_number + 1:
                    "id : " +
                    str(players[player_number][0]) +
                    " | " +
                    players[player_number][1].first_name +
                    " " +
                    players[player_number][1].last_name +
                    " | " + "date de naissance : " +
                    str(players[player_number][1].date_of_birth) +
                    " | " + "sexe : " +
                    str(players[player_number][1].sex) +
                    " | " + "ranking : " +
                    str(players[player_number][1].ranking)
            })
        name = " Rapport de joueurs "
        return name, choices

    @staticmethod
    def order_players_by_name_for_report(players: Dict):
        players_ordered_by_name = sorted(players.items(), key=lambda n: n[1].last_name)
        return players_ordered_by_name

    def display_players_report_by_name(self, players):
        print("players : ", players)
        players_ordered_by_name = self.order_players_by_name_for_report(players)
        print("players_ordered_by_ranking : ", players_ordered_by_name)
        name, choices = self.generate_players_report_list(players_ordered_by_name)
        name = name + "par nom "
        self.view.display_menu(name, choices)

    @staticmethod
    def order_players_by_ranking_for_report(players: Dict):
        players_ordered_by_ranking = sorted(players.items(), key=lambda r: r[1].ranking, reverse=True)
        return players_ordered_by_ranking

    def display_players_report_by_ranking(self, players):
        print("players : ", players)
        players_ordered_by_ranking = self.order_players_by_ranking_for_report(players)
        print("players_ordered_by_ranking : ", players_ordered_by_ranking)
        name, choices = self.generate_players_report_list(players_ordered_by_ranking)
        name = name + "par classement "
        self.view.display_menu(name, choices)

    '''Les menus à afficher'''
    def display_matches_list_menu(self):
        number_of_match_selected = []
        name, choices = self.generate_matches_list(self.all_matches)
        go_to_last_menu_option = len(self.all_matches) + 1
        choices.update({go_to_last_menu_option: "Revenir au menu précédent"})

        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == go_to_last_menu_option:
                run = False
            # elif user_choice != go_to_last_menu_option and user_choice in number_of_match_selected:
            #     message = "Match déjà choisi. Choisissez un autre"
            #     self.view.display_a_simple_message(message)
            else:
                message = f"-- Match {user_choice} choisi --"
                self.view.display_a_simple_message(message)
                self.enter_match_result_menu(user_choice)
                # number_of_match_selected.append(user_choice)

    def display_start_tournament_menu(self):
        name, choices = self.generate_tournaments_list(self.tournaments)
        go_to_last_menu_option = len(self.tournaments)+1
        choices.update({go_to_last_menu_option: "Revenir au menu précédent"})

        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == go_to_last_menu_option:
                run = False
            else:
                self.evaluate_current_tournament_status(user_choice)

    def display_tournaments_management_menu(self):
        choices = {
            1: "Liste de tournois",
            2: "Créer un tournoi",
            3: "Mettre à jour les données d'un tournoi",
            4: "Initier un tournoi",
            5: "Revenir au menu précédent"
        }

        name = "** GESTION DE TOURNOIS **"
        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == 1:
                self.display_tournament_list()
            elif user_choice == 2:
                self.make_new_tournament()
            elif user_choice == 3:
                self.update_tournament_info()
            elif user_choice == 4:
                self.display_start_tournament_menu()
            elif user_choice == 5:
                run = False

    def display_players_management_menu(self):
        choices = {
            1: "Liste de joueurs",
            2: "Ajouter un joueur",
            3: "Mettre à jour les données d'un joueur",
            4: "Revenir au menu précédent"
        }
        name = "** GESTION DE JOUEURS **"
        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == 1:
                # self.view.display_players_list(self.players)
                self.display_players_list()
                # name, choices = self.generate_players_list(self.players)
                # self.view.display_menu(name, choices)
            elif user_choice == 2:
                self.enter_new_player_info()
            elif user_choice == 3:
                self.update_player_info()
            elif user_choice == 4:
                run = False

    def display_players_report_menu(self, players):
        choices = {
            1: "Rapport par ordre descendant",
            2: "Rapport par classement",
            3: "Revenir au menu précédent"
        }
        name = "** CRÉATION DE RAPPORTS **"
        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == 1:
                print('Liste de tous les joueurs')
                self.display_players_report_by_name(players)
            elif user_choice == 2:
                print('Liste des joueurs d un tournoi')
                self.display_players_report_by_ranking(players)
            elif user_choice == 3:
                run = False

    def display_players_report_by_tournament_menu(self):
        pass

    def display_tournament_report(self):
        pass

    def display_tournaments_report(self):
        pass

    def display_reports_menu(self):
        choices = {
            1: "Liste de tous les joueurs",
            2: "Liste des joueurs d'un tournoi",
            3: "Liste de tous les tournois",
            4: "Liste de tous les tours d'un tournoi",
            5: "Liste de tous les matchs d'un tournoi",
            6: "Revenir au menu précédent"
        }
        name = "** CRÉATION DE RAPPORTS **"
        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == 1:
                print('Liste de tous les joueurs')
                self.display_players_report_menu(self.players)
            elif user_choice == 2:
                print('Liste des joueurs d un tournoi')
                self.display_players_report_by_tournament_menu()
            elif user_choice == 3:
                print('Liste de tous les tournois')
                self.display_tournaments_report()
            elif user_choice == 4:
                print('Liste de tous les tours d un tournoi')
            elif user_choice == 5:
                print('Liste de tous les matchs d un tournoi')
            elif user_choice == 6:
                run = False

    def display_data_management_menu(self):
        choices = {
            1: "Sauvegarder les données",
            2: "Charger les données",
            3: "Revenir au menu précédent"
        }
        name = "** SAUVEGARDER/CHARGER LES DONNÉES **"
        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == 1:
                print('Sauvegarder les données')
            elif user_choice == 2:
                print('Charger les données')
            elif user_choice == 3:
                run = False

    def display_main_menu(self):
        choices = {
            1: "Gestion de tournois",
            2: "Gestion de joueurs",
            3: "Création de rapports",
            4: "Sauvegarder/Charger les données",
            5: "Fermer l'application"
        }

        name = "** MENU PRINCIPAL **"
        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == 1:
                self.display_tournaments_management_menu()
            elif user_choice == 2:
                self.display_players_management_menu()
            elif user_choice == 3:
                self.display_reports_menu()
            elif user_choice == 4:
                self.display_data_management_menu()
            elif user_choice == 5:
                message = "***** Application fermée *****"
                self.view.display_a_simple_message(message)
                run = False
            # self.clear_screen()
