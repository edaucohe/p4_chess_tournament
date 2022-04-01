import tinydb.table
from tinydb import TinyDB, Query, where
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
        self.db = TinyDB('db.json')

    # Gestion de tournois
    def create_new_tournament(self):
        # Enter tournament info
        new_tournament = self.view.enter_tournament_info()

        # Add players in new tournament
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

        # Run post-init actions:
        # - generate starting scores
        # - generate next round (so, "rounds list" is no empty)
        # - enter start date
        new_tournament.init()

        # Store tournament in our list
        new_tournament_id = len(self.tournaments) + 1
        self.tournaments[new_tournament_id] = new_tournament
        self.current_tournament = new_tournament

        print("new_tournament : ", new_tournament)
        print("self.tournaments : ", self.tournaments)

    def update_tournament_info(self):
        place = ""
        time_control = ""
        description = ""

        name, choices = self.generate_tournaments_list_for_report(self.tournaments)
        tournament_id = self.view.input_for_menu(choices)

        name = ""
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

    def start_tournament(self):
        message = f"\n** {self.current_tournament.name} **"
        self.view.display_a_simple_message(message)

        self.display_matches_list_menu()

        # evaluate number of matches with results
        number_of_results = 0
        current_round = self.current_tournament.rounds[-1]
        for match in current_round.matches:
            if isinstance(match[0][1], MatchResult):
                number_of_results += 1
        if number_of_results == 4:
            current_round.close()

        print("current_round : ", current_round)
        print("self.current_tournament : ", self.current_tournament)

    def evaluate_current_tournament_status(self, tournament_id_selected):
        self.current_tournament = []
        self.current_tournament = self.tournaments[tournament_id_selected]
        print("self.current_tournament : ", self.current_tournament)
        rounds_in_current_tournament: List[Round] = self.current_tournament.rounds
        current_round: Optional[Round] = \
            rounds_in_current_tournament[-1] if len(rounds_in_current_tournament) > 0 else None

        if current_round.end is None:
            # play current round because matches to be played
            self.start_tournament()
        else:
            # current round has ended
            if len(rounds_in_current_tournament) < self.current_tournament.round_count:
                # generate new round because tournament in progress yet
                self.current_tournament.generate_next_round()
                self.start_tournament()
            else:
                # round 4 has ended, so stop tournament
                message = "\n** Tournoi déjà fini =( **"
                self.view.display_a_simple_message(message)

    def enter_match_result_menu(self, match_selection):
        match = self.current_tournament.rounds[-1].matches[match_selection - 1]
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
        if tournaments:
            name = " Liste de tournois "
            for tournament_number in range(len(tournaments)):
                for round_in_progress in tournaments[tournament_number + 1].rounds:
                    if len(tournaments[tournament_number + 1].rounds) < 4:
                        choices[tournament_number + 1] = tournaments[tournament_number + 1].name
                        name = " Liste de tournois "
                    else:
                        if round_in_progress.end is None:
                            choices[tournament_number + 1] = tournaments[tournament_number + 1].name
                            name = " Liste de tournois "
                        else:
                            name = None
        else:
            name = None
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
            choices[matches.index(match) + 1] = \
                match[0][0].first_name + " " + match[0][0].last_name + " vs " + \
                match[1][0].first_name + " " + match[1][0].last_name

        name = " Liste de matches "
        return name, choices

    def display_matches_list_menu(self):
        name_of_round = self.current_tournament.rounds[-1].name
        self.view.display_a_simple_message(name_of_round)

        name, choices = self.generate_matches_list()
        current_matches = self.current_tournament.rounds[-1].matches
        go_to_last_menu_option = len(current_matches) + 1
        choices[go_to_last_menu_option] = "Revenir au menu précédent"

        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == go_to_last_menu_option:
                run = False
            elif user_choice != go_to_last_menu_option \
                    and not isinstance(current_matches[user_choice - 1][0][1], MatchResult):
                message = f"-- Match {user_choice} choisi --"
                self.view.display_a_simple_message(message)
                self.enter_match_result_menu(user_choice)
            else:
                message = "Match deja choisit ! Choisissez un autre match, svp"
                self.view.display_a_simple_message(message)

    def display_start_tournament_menu(self):
        name, choices = self.generate_tournaments_list(self.tournaments)
        go_to_last_menu_option = len(self.tournaments) + 1
        choices[go_to_last_menu_option] = "Revenir au menu précédent"

        run = True
        if name is None:
            message = "** Il n'y a pas de tournois en cours **"
            self.view.display_a_simple_message(message)
            run = False

        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == go_to_last_menu_option:
                run = False
            else:
                self.evaluate_current_tournament_status(user_choice)

    def display_tournaments_management_menu(self):
        choices = {
            1: "Tournoi en cours",
            2: "Créer un tournoi",
            3: "Mettre à jour les données d'un tournoi",
            4: "Revenir au menu précédent"
            # 5: "Revenir au menu précédent"
        }

        name = "** GESTION DE TOURNOIS **"
        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == 1:
                self.display_start_tournament_menu()
                # self.display_tournament_list()
            elif user_choice == 2:
                self.create_new_tournament()
            elif user_choice == 3:
                self.update_tournament_info()
            elif user_choice == 4:
                run = False
                # self.display_start_tournament_menu()
            # elif user_choice == 5:
            #     run = False

    # Gestion de joueurs
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

    def enter_new_player_info(self):
        id_new_player = len(self.players) + 1
        new_player = self.view.enter_player_info()
        self.players[id_new_player] = new_player

    @staticmethod
    def generate_players_list(players):
        choices = {}
        for player_number in range(len(players)):
            choices[player_number + 1] = players[player_number + 1].first_name + " " + players[
                player_number + 1].last_name

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

    # Gestion de rapports

    @staticmethod
    def generate_players_report_list(players):
        choices = {}
        for player_number in range(len(players)):
            choices[player_number + 1] = \
                "Id : " + str(players[player_number][0]) + \
                " | " + players[player_number][1].first_name + " " + players[player_number][1].last_name + \
                " | " + "Date de naissance : " + str(players[player_number][1].date_of_birth) + \
                " | " + "Sexe : " + str(players[player_number][1].sex) + \
                " | " + "Ranking : " + str(players[player_number][1].ranking)

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

    @staticmethod
    def generate_tournaments_list_for_report(tournaments):
        choices = {}
        for tournament_number in range(len(tournaments)):
            choices[tournament_number + 1] = tournaments[tournament_number + 1].name

        name = " Liste de tournois "
        return name, choices

    def display_players_report_by_tournament_menu(self):
        name, choices = self.generate_tournaments_list_for_report(self.tournaments)
        go_to_last_menu_option = len(self.tournaments) + 1
        choices[go_to_last_menu_option] = "Revenir au menu précédent"

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
            choices[tournament_number + 1] = \
                tournaments[tournament_number + 1].name + " | " + "Lieu : " + \
                tournaments[tournament_number + 1].place + " | " + "Type de contrôle : " + \
                str(tournaments[tournament_number + 1].time_control.value) + " | " + "Description : " + \
                tournaments[tournament_number + 1].description

        name = " Liste de tournois "
        return name, choices

    def display_tournaments_report(self):
        name, choices = self.generate_tournaments_report(self.tournaments)
        self.view.display_menu(name, choices)
        return choices

    @staticmethod
    def generate_rounds_report(current_tournament):
        rounds_in_current_tournament = current_tournament.rounds
        choices = {"Tournoi :": current_tournament.name}

        for round_in_current_tournament in rounds_in_current_tournament:
            if round_in_current_tournament.end is None:
                message = "Round encore en cours"
            else:
                message = str(round_in_current_tournament.end)

            choices[str(round_in_current_tournament.name)] = \
                "| " + "Date de début : " + str(round_in_current_tournament.start) + \
                " | " + "Date de fin : " + message

        name = " Rapports de rounds "
        return name, choices

    def display_rounds_report(self, tournament_id_selected):
        self.current_tournament = []
        self.current_tournament = self.tournaments.get(tournament_id_selected)
        name, choices = self.generate_rounds_report(self.current_tournament)
        self.view.make_common_report_for_rounds_and_matches(name, choices)

    def display_rounds_report_menu(self):
        name, choices = self.generate_tournaments_list_for_report(self.tournaments)
        go_to_last_menu_option = len(self.tournaments) + 1
        choices[go_to_last_menu_option] = "Revenir au menu précédent"

        run = True
        while run:
            self.view.display_menu(name, choices)
            user_choice = self.view.input_for_menu(choices)
            if user_choice == go_to_last_menu_option:
                run = False
            else:
                self.display_rounds_report(user_choice)

    def generate_matches_report(self):
        rounds_in_current_tournament = self.current_tournament.rounds
        choices = {"Tournoi :": self.current_tournament.name}

        for round_in_current_tournament in rounds_in_current_tournament:
            number_of_match = 1
            for match_in_current_round in round_in_current_tournament.matches:
                message_of_result = ""
                first_name_p1 = match_in_current_round[0][0].first_name
                last_name_p1 = match_in_current_round[0][0].last_name
                first_name_p2 = match_in_current_round[1][0].first_name
                last_name_p2 = match_in_current_round[1][0].last_name

                if isinstance(match_in_current_round[0][1], MatchResult):
                    if match_in_current_round[0][1].name == "WIN":
                        message_of_result += "Résultat : 1 - 0"
                    elif match_in_current_round[0][1].name == "LOSS":
                        message_of_result += "Résultat : 0 - 1"
                    elif match_in_current_round[0][1].name == "DRAW":
                        message_of_result += "Résultat : 0.5 - 0.5"

                    choices[str(round_in_current_tournament.name) + " | " + "Match " + str(number_of_match)] = \
                        "| " + first_name_p1 + " " + last_name_p1 + " vs " + \
                        first_name_p2 + " " + last_name_p2 + " | " + \
                        message_of_result

                    number_of_match += 1

        name = " Rapports de matches "
        return name, choices

    def display_matches_report(self, tournament_id_selected):
        self.current_tournament = self.tournaments[tournament_id_selected]
        name, choices = self.generate_matches_report()
        self.view.make_common_report_for_rounds_and_matches(name, choices)

    def display_matches_report_menu(self):
        name, choices = self.generate_tournaments_list_for_report(self.tournaments)
        go_to_last_menu_option = len(self.tournaments) + 1
        choices[go_to_last_menu_option] = "Revenir au menu précédent"

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

    # Gestion de la base de données
    def save_database(self):
        # I need to:
        # - Save player/tournament datas. If they exist, update data: If not, add new datas.
        players_table = self.db.table('players')

        print("players_table BEFORE update: ", players_table)
        docs = players_table.search(where('ranking') > 0)
        info_players = []
        for doc in docs:
            print("doc : ", doc)
            print("doc.doc_id : ", doc.doc_id)
            info_players.append(doc)

        for index, player in self.players.items():
            current_player_data = players_table.contains(doc_id=index)
            if current_player_data:
                if info_players[index-1] != player.to_json():
                    players_table.update(player.to_json(), where('first_name') == info_players[index - 1]["first_name"])
            else:
                players_table.insert(player.to_json())

        print("players_table AFTER update: ", players_table)
        docs = players_table.search(where('ranking') > 0)
        for doc in docs:
            print("doc.doc_id : ", doc.doc_id)
            print("doc : ", doc)

        # tournaments_table = self.db.table('tournaments')

    def load_database(self):
        self.db.drop_table('players')
        self.db.drop_table('players_database')
        self.db.drop_table('tournaments')

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
                self.save_database()
            elif user_choice == 2:
                print('Charger les données')
                self.load_database()
            elif user_choice == 3:
                run = False

    # Menu principal
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
