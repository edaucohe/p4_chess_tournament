from typing import List, Dict, Optional

from chess.views import TerminalView
from chess.models import Player, Tournament, DEFAULT_PLAYERS_NUMBER, Round, MatchResult


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
            view: Optional[TerminalView] = None):
        self.players = players or dict()
        self.tournaments = tournaments or dict()
        self.current_tournament = current_tournament or None
        self.view = view or TerminalView()

    '''Gestion de tournois'''

    def create_new_tournament(self):
        # Enter tournament info
        new_tournament = self.view.enter_tournament_info()

        # Add players to it
        selected_players = {}
        choices = self.display_players_list()
        for player_number in range(DEFAULT_PLAYERS_NUMBER):
            player_id = self.view.input_for_menu(choices, header='Choisissez un joueur')
            while player_id in selected_players:
                message = "choisissez un autre joueur !"
                self.view.display_a_simple_message(message)
                player_id = self.view.input_for_menu(choices)

            selected_players[player_id] = self.players[player_id]
        new_tournament.players = selected_players

        # Run post-init actions
        new_tournament.generate_scores()
        new_tournament.init()

        # Store tournament in our list
        new_tournament_id = len(self.tournaments) + 1
        self.tournaments.update({new_tournament_id: new_tournament})
        self.current_tournament = new_tournament

        print("new_tournament : ", new_tournament)
        print("self.tournaments : ", self.tournaments)

    def update_tournament_info(self):
        name = ""
        place = ""
        time_control = ""
        description = ""

        choices = self.display_tournament_list()
        tournament_id = self.view.input_for_menu(choices)

        tournament_selected = self.tournaments[tournament_id]
        number_of_data = 4
        for data in range(number_of_data):
            if data == 0:
                name = self.view.enter_tournament_name()
                if name == "":
                    name = tournament_selected.name
            elif data == 1:
                place = self.view.enter_tournament_place()
                if place == "":
                    place = tournament_selected.place
            elif data == 2:
                time_control = self.view.enter_tournament_time_control()
                if time_control is None:
                    time_control = tournament_selected.time_control
            elif data == 3:
                description = self.view.enter_tournament_description()
                if description == "":
                    description = tournament_selected.description

        tournament_selected.update_tournament(name, place, time_control, description)

    # TODO move me in the tournament model
    # @staticmethod
    # def make_list_of_matches(players_in_group):
    #     matches = []
    #     matches_by_group = []
    #     for player_in_group in players_in_group:
    #         print("player_in_group : ", player_in_group)
    #         matches.append(player_in_group)
    #         if len(matches) == 2:
    #             matches_by_group.append(matches)
    #             matches = []
    #     return matches_by_group

    # def evaluate_if_matches_repeated(self, number_of_exchange_done):
    #     matches_already_played = []
    #     # print("matches_already_played - quand on initialise : ", matches_already_played)
    #     # print("len(matches_already_played) - quand on initialise : ", len(matches_already_played))
    #     match_already_played = False
    #
    #     for match in self.all_matches:
    #         index_of_current_match = self.all_matches.index(match)
    #         # print("index_of_current_match : ", index_of_current_match)
    #         # print("self.all_matches : ", self.all_matches)
    #         # print("match : ", match)
    #         p1 = match[0][0]
    #         p2 = match[1][0]
    #         match_to_play = (p1, p2)
    #
    #         if match_to_play in self.matches_already_played:
    #             match_already_played = True
    #             # print("match_to_play (deja joué) : ", match_to_play)
    #             self.exchange_players(index_of_current_match, number_of_exchange_done)
    #         else:
    #             matches_already_played.append((p1, p2))
    #             matches_already_played.append((p2, p1))
    #             # print("match_to_play (p1, p2) : ", (p1, p2))
    #             # print("match_to_play (p2, p1) : ", (p2, p1))
    #             # print("matches_already_played : ", matches_already_played)
    #
    #         if self.all_matches.index(match) == 3 and match_already_played is False:
    #             self.matches_already_played.extend(matches_already_played)
    #             # print("self.matches_already_played () : ", self.matches_already_played)
    #             # print("len(self.matches_already_played) () : ", len(self.matches_already_played))
    #             self.number_of_exchange_done = 0
    #             return match_already_played, self.number_of_exchange_done
    #
    #     return match_already_played, self.number_of_exchange_done
    #
    #     # print("self.matches_already_played : ", self.matches_already_played)
    #     # print("matches_already_played : ", matches_already_played)
    #
    # def exchange_players(self, index_of_current_match, number_of_exchange_done):
    #     self.number_of_exchange_done += 1
    #     print("self.number_of_exchange_done : ", self.number_of_exchange_done)
    #     print("index_of_current_match : ", index_of_current_match)
    #     if self.number_of_exchange_done % 2 == 1:
    #         print("self.all_matches[index_of_current_match][1] : ", self.all_matches[index_of_current_match][1])
    #         print("self.all_matches[index_of_current_match+1][0] : ", self.all_matches[index_of_current_match + 1][0])
    #         self.all_matches[index_of_current_match][1], self.all_matches[index_of_current_match + 1][0] = \
    #             self.all_matches[index_of_current_match + 1][0], self.all_matches[index_of_current_match][1]
    #     elif self.number_of_exchange_done % 2 == 0:
    #         print("self.all_matches[index_of_current_match][1] : ", self.all_matches[index_of_current_match][1])
    #         print("self.all_matches[index_of_current_match+1][1] : ", self.all_matches[index_of_current_match + 1][1])
    #         self.all_matches[index_of_current_match][1], self.all_matches[index_of_current_match + 1][1] = \
    #             self.all_matches[index_of_current_match + 1][1], self.all_matches[index_of_current_match][1]
    #     # if self.number_of_exchange_done % 4 == 3:
    #     #     print("self.all_matches[index_of_current_match][1] : ", self.all_matches[index_of_current_match][1])
    #     #     print("self.all_matches[index_of_current_match+2][0] : ", self.all_matches[index_of_current_match+2][0])
    #     #     self.all_matches[index_of_current_match][1], self.all_matches[index_of_current_match+2][0] = \
    #     #         self.all_matches[index_of_current_match+2][0], self.all_matches[index_of_current_match][1]
    #     # elif self.number_of_exchange_done % 4 == 0:
    #     #     print("self.all_matches[index_of_current_match][1] : ", self.all_matches[index_of_current_match][1])
    #     #     print("self.all_matches[index_of_current_match+2][1] : ", self.all_matches[index_of_current_match+2][1])
    #     #     self.all_matches[index_of_current_match][1], self.all_matches[index_of_current_match+2][1] = \
    #     #         self.all_matches[index_of_current_match+2][1], self.all_matches[index_of_current_match][1]

    def start_tournament(self):
        # n = 0
        # score = 0
        print("self.current_tournament.players : ", self.current_tournament.players)
        print("self.current_tournament.scores : ", self.current_tournament.scores)

        self.display_matches_list_menu()

        number_of_results = 0
        current_round = self.current_tournament.rounds[-1]
        print("current_round before : ", current_round)
        for match in current_round.matches:
            if isinstance(match[0][1], MatchResult):
                number_of_results += 1
            else:
                pass

        print("number_of_results : ", number_of_results)
        if number_of_results == 4:
            current_round.close()
            self.current_tournament.init()

        print("current_round after : ", current_round)
        print("self.current_tournament : ", self.current_tournament)

        # # TODO Code pour générer des scores pour les joueurs
        # for player_id, player in self.current_tournament.players.items():
        #     players_with_score.append([player, score])
        #     if n % 3 == 0:
        #         score = 1
        #     elif n % 3 == 1:
        #         score = 0
        #     else:
        #         score = 0.5
        #     # if n % 2 == 0:
        #     #     score = 1
        #     # else:
        #     #     score = 0
        #     n += 1
        # # TODO jusqu'ici

            # self.players_in_groups = players_in_groups
        # elif not self.number_of_matches_played:
        #     print("la liste est vide : ", self.number_of_matches_played)
        #     players_in_groups = self.classify_players_in_groups()
        #     current_round =

        # players_in_groups = self.classify_players_in_groups()
        # print("players_in_groups : ", players_in_groups)

        # message = f"-- {self.current_tournament.rounds[-1].__getattribute__('name')} --"
        # self.view.display_a_simple_message(message)
        #
        # if len(self.current_tournament.rounds) == 1:
        #     self.all_matches = self.tournament_management_round_one(players_in_groups)
        #     self.players_in_groups = players_in_groups
        # else:
        #     self.all_matches = self.matches_by_round_management(players_in_groups)
        #     self.players_in_groups = players_in_groups
        #
        # print("all_matches = ", self.all_matches)
        #
        # if self.evaluation_of_matches:
        #     self.number_of_exchange_done = 0
        #     match_already_played, number_of_exchange_done = self.evaluate_if_matches_repeated(
        #         self.number_of_exchange_done)
        #     # print("match_already_played : ", match_already_played)
        #
        #     number_of_exchange_done = 0
        #     while match_already_played:
        #         '''refaire les matches'''
        #         match_already_played, number_of_exchange_done = \
        #             self.evaluate_if_matches_repeated(number_of_exchange_done)

                # for next_match in range(3):
                #     for next_player in range(2):
                #         self.all_matches = self.exchange_players(next_match, next_player)
        # else:
        #     print("les matches ont été deja évalués au moins une fois !!! on est aussi entré au display menu")

        # else:
        #     '''laisser les matchs créés'''

        # '''Voulez-vous entrer les résultats d un match ?'''
        # self.display_matches_list_menu()
        #
        # if len(self.number_of_matches_played) == 4:
        #     self.evaluation_of_matches = True
        #     # print(f"la liste a bien {len(self.number_of_matches_played)} elements : ", self.number_of_matches_played)
        #     # print("il va falloir réinitialiser les variables pour passer au prochain ROUND")
        #     # print("Marquer le Round comme terminé")
        #     # print("Round.end : ", Round.end)
        #     Round.end = datetime.now
        #     # print("Round.end : ", Round.end)
        #
        #     '''Pour le nouveau Round'''
        #     # print("len(self.current_tournament.rounds) : ", len(self.current_tournament.rounds))
        #     # print("self.current_tournament.rounds[-1].end : ", self.current_tournament.rounds[-1].end)
        #     self.current_tournament.rounds[-1].end = datetime.now()
        #     # print("NEW self.current_tournament.rounds[-1].end : ", self.current_tournament.rounds[-1].end)
        #
        #     if len(self.current_tournament.rounds) == self.current_tournament.round_count:
        #         print("DEJA ENTRÉ self.current_tournament.rounds[-1].end : ", self.current_tournament.rounds[-1].end)
        #     else:
        #         # self.current_tournament.rounds.append(self.view.enter_round_info(end_date=None))
        #         round_name = f"ROUND {len(self.current_tournament.rounds) + 1}"
        #         # print(round_name)
        #         self.current_tournament.rounds.append(self.view.enter_new_round(round_name))
        #
        #     # self.current_tournament.rounds.append(self.view.enter_round_info(end_date=None))
        #     # self.view.round_finished()
        #
        #     # print("self.view.round_finished() : ", self.round.end.value)
        #
        #     # players_in_groups = []
        #     # self.players_in_groups = players_in_groups
        #     self.number_of_matches_played = []
        #     self.matches_played_in_current_round = []
        # print("list_of_matches : ", list_of_matches)
        # print("new_all_matches : ", new_all_matches)

        # current_round = self.enter_round_info()

        # if round_number == 1:
        #     pass

    def evaluate_current_tournament_status(self, tournament_id_selected):
        self.current_tournament = []
        self.current_tournament = self.tournaments[tournament_id_selected]
        print("self.current_tournament : ", self.current_tournament)
        rounds_in_current_tournament: List[Round] = self.tournaments[tournament_id_selected].rounds
        current_round: Optional[Round] = \
            rounds_in_current_tournament[-1] if len(rounds_in_current_tournament) > 0 else None

        if current_round is None:
            # There is no round in current tournament
            message = "round pas encore généré"
            self.view.display_a_simple_message(message)
        elif current_round is not None and rounds_in_current_tournament[-1].end is None:
            # current round in current tournament
            message = f"\n** {self.current_tournament.name} **"
            self.view.display_a_simple_message(message)
            self.start_tournament()
        elif current_round is not None and rounds_in_current_tournament[-1].end is not None:
            # current tournament is ended
            message = "\n** Tournoi déjà fini =( **"
            self.view.display_a_simple_message(message)

    # def enter_match_result(self, player_one, player_two, match_result_selection, match_selection):
    #     list_of_matches = self.current_tournament.rounds[-1].__getattribute__("matches")
    #
    #     if match_result_selection == 1:
    #         message = f"{player_one[0].first_name + ' ' + player_one[0].last_name} a gagné le match"
    #         self.view.display_a_simple_message(message)
    #         self.number_of_matches_played.append(match_selection)
    #         self.current_tournament.scores.update(
    #             {player_one[0]: self.current_tournament.scores.get(player_one[0]) + 1})
    #         match = ([player_one[0], MatchResult.WIN], [player_two[0], MatchResult.LOSS])
    #         self.matches_played_in_current_round.append(match)
    #         # print("self.matches_played_in_current_round : ", self.matches_played_in_current_round)
    #         # print("self.current_tournament.rounds :", self.current_tournament.rounds[-1])
    #         self.current_tournament.rounds[-1] = self.view.enter_round_match(
    #             self.matches_played_in_current_round, self.current_tournament.rounds[-1].__getattribute__("name"))
    #         # print("self.current_tournament.rounds :", self.current_tournament.rounds)
    #
    #     elif match_result_selection == 2:
    #         message = f"{player_two[0].first_name + ' ' + player_two[0].last_name} a gagné le match"
    #         self.view.display_a_simple_message(message)
    #         self.number_of_matches_played.append(match_selection)
    #         self.current_tournament.scores.update(
    #             {player_two[0]: self.current_tournament.scores.get(player_two[0]) + 1})
    #         match = ([player_one[0], MatchResult.LOSS], [player_two[0], MatchResult.WIN])
    #         self.matches_played_in_current_round.append(match)
    #         # print("self.matches_played_in_current_round : ", self.matches_played_in_current_round)
    #         # print("self.current_tournament.rounds[-1] :", self.current_tournament.rounds[-1])
    #         self.current_tournament.rounds[-1] = self.view.enter_round_match(
    #             self.matches_played_in_current_round, self.current_tournament.rounds[-1].__getattribute__("name"))
    #         # print("self.current_tournament.rounds :", self.current_tournament.rounds)
    #
    #     elif match_result_selection == 3:
    #         message = "Les joueurs ont fait un match nul"
    #         self.view.display_a_simple_message(message)
    #         self.number_of_matches_played.append(match_selection)
    #         self.current_tournament.scores.update(
    #             {player_one[0]: self.current_tournament.scores.get(player_one[0]) + 0.5})
    #         self.current_tournament.scores.update(
    #             {player_two[0]: self.current_tournament.scores.get(player_two[0]) + 0.5})
    #         match = ([player_one[0], MatchResult.DRAW], [player_two[0], MatchResult.DRAW])
    #         self.matches_played_in_current_round.append(match)
    #         # print("self.matches_played_in_current_round : ", self.matches_played_in_current_round)
    #         # print("self.current_tournament.rounds :", self.current_tournament.rounds[-1])
    #         self.current_tournament.rounds[-1] = self.view.enter_round_match(
    #             self.matches_played_in_current_round, self.current_tournament.rounds[-1].__getattribute__("name"))
    #         # print("self.current_tournament.rounds :", self.current_tournament.rounds)
    #
    #     print("list_of_matches : ", list_of_matches)

    def enter_match_result_menu(self, match_selection):
        match = self.current_tournament.rounds[-1].matches[match_selection-1]
        player_one = match[0]
        player_two = match[1]
        choices = {
            1: player_one[0].first_name + " " + player_one[0].last_name,
            2: player_two[0].first_name + " " + player_two[0].last_name,
            3: "Match null",
            4: "Revenir au menu précédent"
        }
        name = " Qui a gagné le match ? "

        self.view.display_menu(name, choices)
        user_choice = self.view.input_for_menu(choices)
        if user_choice == 4:
            pass
        else:
            message = self.current_tournament.enter_match_result(match, user_choice)
            print("self.current_tournament : ", self.current_tournament)
            self.view.display_a_simple_message(message)

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

    def generate_matches_list(self):
        choices = {}
        matches = self.current_tournament.rounds[-1].matches
        print("matches : ", matches)
        for match in matches:
            choices.update({
                matches.index(match)+1:
                    match[0][0].first_name + " " +
                    match[0][0].last_name +
                    " vs " +
                    match[1][0].first_name + " " +
                    match[1][0].last_name
            })

        # for match_number in range(len(matches)):
        #     choices.update({
        #         match_number + 1:
        #             self.current_tournament.rounds[match_number].matches[0][0].first_name + " " +
        #             self.current_tournament.rounds[match_number][0][0].last_name +
        #             " vs " +
        #             self.current_tournament.rounds[match_number][1][0].first_name + " " +
        #             self.current_tournament.rounds[match_number][1][0].last_name})

        name = " Liste de matches "
        return name, choices

    def display_matches_list_menu(self):
        name_of_round = self.current_tournament.rounds[-1].name
        self.view.display_a_simple_message(name_of_round)

        name, choices = self.generate_matches_list()
        current_matches = self.current_tournament.rounds[-1].matches
        go_to_last_menu_option = len(current_matches) + 1
        choices.update({go_to_last_menu_option: "Revenir au menu précédent"})

        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == go_to_last_menu_option:
                run = False
            elif user_choice != go_to_last_menu_option \
                    and not isinstance(current_matches[user_choice-1][0][1], MatchResult):
                message = f"-- Match {user_choice} choisi --"
                self.view.display_a_simple_message(message)
                self.enter_match_result_menu(user_choice)
            else:
                message = "Match deja choisit ! Choisissez un autre match, svp"
                self.view.display_a_simple_message(message)

    def display_start_tournament_menu(self):
        name, choices = self.generate_tournaments_list(self.tournaments)
        go_to_last_menu_option = len(self.tournaments) + 1
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
                self.create_new_tournament()
            elif user_choice == 3:
                self.update_tournament_info()
            elif user_choice == 4:
                self.display_start_tournament_menu()
            elif user_choice == 5:
                run = False

    # def enter_one_player_data(self):
    #     return data

    '''Gestion de joueurs'''

    def update_player_info(self):
        first_name = ""
        last_name = ""
        date_of_birth = None
        sex = None
        ranking = None

        choices = self.display_players_list()
        player_id_selected = self.view.input_for_menu(choices)

        player_selected = self.players[player_id_selected]
        number_of_data = 5
        for data in range(number_of_data):
            if data == 0:
                first_name = self.view.enter_first_name_data()
                if first_name == "":
                    first_name = player_selected.first_name
            elif data == 1:
                last_name = self.view.enter_last_name_data()
                if last_name == "":
                    last_name = player_selected.last_name
            elif data == 2:
                date_of_birth = self.view.enter_birth_data()
                if date_of_birth is None:
                    date_of_birth = player_selected.date_of_birth
            elif data == 3:
                sex = self.view.enter_sex_data()
                if sex is None:
                    sex = player_selected.sex
            elif data == 4:
                ranking = self.view.enter_ranking_data()
                if ranking is None:
                    ranking = player_selected.ranking

        player_selected.update_player(first_name, last_name, date_of_birth, sex, ranking)
        print("player_selected : ", player_selected)

        # player = self.view.update_player_info(first_name, last_name, date_of_birth, sex, ranking)
        # self.players[player_id_selected] = player

    def enter_new_player_info(self):
        id_new_player = len(self.players) + 1
        new_player = self.view.enter_player_info()
        self.players[id_new_player] = new_player

    @staticmethod
    def generate_players_list(players):
        choices = {}
        for player_number in range(len(players)):
            choices.update({
                player_number+1:
                    players[player_number+1].first_name + " " + players[player_number+1].last_name
            })
        name = " Liste de joueurs "
        return name, choices

    def display_players_list(self):
        name, choices = self.generate_players_list(self.players)
        self.view.display_menu(name, choices)
        return choices

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
                self.display_players_list()
            elif user_choice == 2:
                self.enter_new_player_info()
            elif user_choice == 3:
                self.update_player_info()
            elif user_choice == 4:
                run = False

    '''Gestion de rapports'''

    @staticmethod
    def generate_players_report_list(players):
        choices = {}
        for player_number in range(len(players)):
            choices.update({
                player_number + 1:
                    "Id : " +
                    str(players[player_number][0]) +
                    " | " +
                    players[player_number][1].first_name +
                    " " +
                    players[player_number][1].last_name +
                    " | " + "Date de naissance : " +
                    str(players[player_number][1].date_of_birth) +
                    " | " + "Sexe : " +
                    str(players[player_number][1].sex) +
                    " | " + "Ranking : " +
                    str(players[player_number][1].ranking)
            })
        name = " Rapport de joueurs "
        return name, choices

    @staticmethod
    def players_sorted_alphabetically(players: Dict):
        return sorted(players.items(), key=lambda n: n[1].last_name)

    def display_players_report_by_name(self, players):
        sorted_players = self.players_sorted_alphabetically(players)
        name, choices = self.generate_players_report_list(sorted_players)
        name = name + "par nom "
        self.view.display_menu(name, choices)

    def display_players_report_by_ranking(self, players):
        sorted_players = sorted(players.items(), key=lambda r: r[1].ranking, reverse=True)
        name, choices = self.generate_players_report_list(sorted_players)
        name = name + "par classement "
        self.view.display_menu(name, choices)

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
                self.display_players_report_by_name(players)
            elif user_choice == 2:
                self.display_players_report_by_ranking(players)
            elif user_choice == 3:
                run = False

    def display_players_report_by_tournament_menu(self):
        name, choices = self.generate_tournaments_list(self.tournaments)
        go_to_last_menu_option = len(self.tournaments) + 1
        choices.update({go_to_last_menu_option: "Revenir au menu précédent"})

        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == go_to_last_menu_option:
                run = False
            else:
                players_of_current_tournament = self.tournaments.get(user_choice).players
                self.display_players_report_menu(players_of_current_tournament)

    @staticmethod
    def generate_tournaments_report(tournaments):
        choices = {}
        for tournament_number in range(len(tournaments)):
            choices.update({
                tournament_number + 1:
                    tournaments.get(tournament_number + 1).name +
                    " | " + "Lieu : " +
                    tournaments.get(tournament_number + 1).place +
                    " | " + "Type de contrôle : " +
                    tournaments.get(tournament_number + 1).time_control +
                    " | " + "Description : " +
                    tournaments.get(tournament_number + 1).description
            })
        name = " Liste de tournois "
        return name, choices

    def display_tournaments_report(self):
        print("self.tournaments : ", self.tournaments)
        name, choices = self.generate_tournaments_report(self.tournaments)
        self.view.display_menu(name, choices)
        return choices

    @staticmethod
    def generate_rounds_report(current_tournament):
        rounds_in_current_tournament = current_tournament.rounds
        choices = {"Tournoi :": current_tournament.__getattribute__("name")}

        for round_in_current_tournament in rounds_in_current_tournament:
            if round_in_current_tournament.__getattribute__('end') is None:
                message = "Round encore en cours"
            else:
                message = str(round_in_current_tournament.__getattribute__('end'))
            choices.update({
                str(round_in_current_tournament.__getattribute__('name')):
                    "| " + "Date de début : " +
                    str(round_in_current_tournament.__getattribute__('start')) +
                    " | " + "Date de fin : " +
                    message
            })

        name = " Rapports de rounds "
        return name, choices

    def display_rounds_report(self, tournament_id_selected):
        self.current_tournament = []
        self.current_tournament = self.tournaments.get(tournament_id_selected)
        name, choices = self.generate_rounds_report(self.current_tournament)
        self.view.make_common_report_for_rounds_and_matches(name, choices)

    def display_rounds_report_menu(self):
        name, choices = self.generate_tournaments_list(self.tournaments)
        go_to_last_menu_option = len(self.tournaments) + 1
        choices.update({go_to_last_menu_option: "Revenir au menu précédent"})

        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == go_to_last_menu_option:
                run = False
            else:
                self.display_rounds_report(user_choice)

    @staticmethod
    def generate_matches_report(current_tournament):
        rounds_in_current_tournament = current_tournament.rounds
        choices = {"Tournoi :": current_tournament.__getattribute__("name")}

        for round_in_current_tournament in rounds_in_current_tournament:
            number_of_match = 1

            for match_in_current_round in round_in_current_tournament.__getattribute__("matches"):
                message_of_result = ""
                first_name_p1 = match_in_current_round[0][0].__getattribute__("first_name")
                last_name_p1 = match_in_current_round[0][0].__getattribute__("last_name")
                first_name_p2 = match_in_current_round[1][0].__getattribute__("first_name")
                last_name_p2 = match_in_current_round[1][0].__getattribute__("last_name")

                if match_in_current_round[0][1].name == "WIN":
                    message_of_result += "Résultat : 1 - 0"
                elif match_in_current_round[0][1].name == "LOSS":
                    message_of_result += "Résultat : 0 - 1"
                elif match_in_current_round[0][1].name == "DRAW":
                    message_of_result += "Résultat : 0.5 - 0.5"

                choices.update({
                    str(round_in_current_tournament.__getattribute__('name')) + " | " + "Match " + str(number_of_match):
                        "| " +
                        first_name_p1 + " " + last_name_p1 +
                        " vs " +
                        first_name_p2 + " " + last_name_p2 +
                        " | " +
                        message_of_result
                })

                number_of_match += 1

        name = " Rapports de matches "
        return name, choices

    def display_matches_report(self, tournament_id_selected):
        self.current_tournament = []
        self.current_tournament = self.tournaments.get(tournament_id_selected)
        name, choices = self.generate_matches_report(self.current_tournament)
        self.view.make_common_report_for_rounds_and_matches(name, choices)

    def display_matches_report_menu(self):
        name, choices = self.generate_tournaments_list(self.tournaments)
        go_to_last_menu_option = len(self.tournaments) + 1
        choices.update({go_to_last_menu_option: "Revenir au menu précédent"})

        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == go_to_last_menu_option:
                run = False
            else:
                self.display_matches_report(user_choice)

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
                self.display_players_report_menu(self.players)
            elif user_choice == 2:
                self.display_players_report_by_tournament_menu()
            elif user_choice == 3:
                self.display_tournaments_report()
            elif user_choice == 4:
                self.display_rounds_report_menu()
            elif user_choice == 5:
                self.display_matches_report_menu()
            elif user_choice == 6:
                run = False

    '''Gestion de la base de données'''

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

    '''Menu principal'''

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
