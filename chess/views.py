import csv
from dataclasses import fields, asdict
from datetime import date
from typing import Any, Callable, List, Dict
# from dataclasses import dataclass, asdict  # , field

from chess.models import Player, Sex, MainMenu, ReportMenu, NewPlayerMenu, NewTournamentMenu, ModifyTournamentMenu, \
    ModifyPlayerInfoMenu, StartTournamentMenu, MENU_OPTION, Tournament, TimeControlKind, DEFAULT_PLAYERS_NUMBER, \
    PlayerScore, SCORE_INIT, PlayerManagementMenu, TournamentManagementMenu, SaveData, MatchResult, \
    MakeNewTournamentMenu, OrderPlayerList, NUMBER_MAX_OF_HEADS, AllPlayersReportMenu, PlayersByTournamentReportMenu


# @dataclass
# class InfoPlayers:
#     info_players = {}  # : Dict = field(init=False)
#     players_list = []  # : List = field(init=False)
#     players_points = 0
#     players_score = 0
#
#     # def __post_init__(self):
#     #     self.info_players = {}
#     #     self.players_list = []
#
#     def get_players_info(self) -> Dict:
#         print("Merci de taper les coordonnées des joueurs : ")
#         self.info_players = asdict(
#             Player(
#                 input("Prénom : "),
#                 input("Nom : "),
#                 input("Date de naissance : "),
#                 input("Sexe : "),
#                 int(input("Classement : "))
#             )
#         )
#
#         return self.info_players
#
#     def get_players_points(self):
#         self.players_points = Points.points
#         return self.players_points
#
#     def get_players_score(self):
#         self.players_score = Score(float(input("Points : ")))
#         return self.players_score
#
#     def show_players(self, players_list):
#         self.players_list = players_list
#         print("---- Info des joueurs (dans le view) ----")
#         print(self.players_list)


def input_with_constraint(desc: str, parse_fn: Callable[[str], Any]):
    while True:
        try:
            input_value = input(desc)
            return parse_fn(input_value)
        # except Exception as error:
        #     print("Merci de respecter le bon format : ", type(error))
        #     if error == ValueError:
        #         print("Merci de respecter le bon format")
        #     elif error == AssertionError:
        #         print("La valeur doit être un numéro positif")
        except ValueError:
            print("Merci de respecter le bon format")
        except AssertionError:
            print("La valeur doit être un numéro positif")


def parse_positive_int(input_as_str: str) -> int:
    value: int = int(input_as_str)
    assert value > 0
    return value


class TerminalView:
    option_selected = MENU_OPTION

    # @staticmethod
    # def display_menu_with_input(name: str, choices: Dict[int, str]):
    #     print(f'\n**** {name} **** ')
    #     for choice_index, choice_name in choices.items():
    #         print(f'{choice_index} - {choice_name}')
    #
    #     # user_input = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
    #     # is_input_valid = user_input in choices
    #     #
    #     # while not is_input_valid:
    #     #     user_input = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
    #     #     is_input_valid = user_input in choices
    #     #
    #     # return user_input

    @staticmethod
    def display_menu(name: str, choices: Dict[int, str]):
        print(f'\n**{name}**')
        for choice_index, choice_name in choices.items():
            print(f'{choice_index} - {choice_name}')

    @staticmethod
    def input_for_menu(choices: Dict[int, str]):
        user_input = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
        is_input_valid = user_input in choices

        while not is_input_valid:
            user_input = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            is_input_valid = user_input in choices

        return user_input

    def display_close_message(self):
        print('***** Closing, Byyyye *****')

    ######### DELETE FROM HERE
    def display_main_menu(self):
        main_menu = MainMenu
        main_menu_options = {
            1: "Gestion de tournois",
            2: "Gestion de joueurs",
            3: "Création de rapports",
            4: "Sauvegarder/Charger les données",
            5: "Fermer l'application"
        }
        # print("Valeur de main_menu : ", main_menu)
        print("\n**** MENU PRINCIPAL ****")
        for key in main_menu_options.keys():
            print(f'{key}) {main_menu_options[key]}')

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            if selection_menu == main_menu.TOURNAMENT_MANAGEMENT.value:
                self.display_tournament_management_menu()
                option = False
            elif selection_menu == main_menu.PLAYERS_MANAGEMENT.value:
                self.display_players_management_menu()
                option = False
            elif selection_menu == main_menu.MAKE_REPORTS.value:
                self.display_make_reports_menu()
                option = False
            elif selection_menu == main_menu.SAVE_DATA.value:
                self.display_save_data_menu()
                option = False
            elif selection_menu == main_menu.CLOSE_APPLI.value:
                print("** Fermeture de l'application **")
                self.option_selected = "close_script"
                option = False
            else:
                print("-- Choisissez une option parmi les proposées ! --")
                option = True

        #     print("valeur de menu_option du MAIN WHILE : ", self.option_selected)
        # print("valeur de menu_option du MAIN HORS WHILE : ", self.option_selected)
        return self.option_selected

    def display_tournament_management_menu(self):
        print("display_tournament_management_menu")
        tournament_management_menu = TournamentManagementMenu
        tournament_management_options = {
            1: "Liste de tournois",
            2: "Créer un tournoi",
            3: "Initier un tournoi",
            4: "Mettre à jour les données d'un tournoi",
            5: "Revenir au menu précédent"
        }
        print("\n**** GESTION DE TOURNOIS ****")
        for key in tournament_management_options.keys():
            print(f'{key}) {tournament_management_options[key]}')

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            if selection_menu == tournament_management_menu.TOURNAMENTS_LIST.value:
                # self.display_tournaments_list()
                self.option_selected = "TOURNAMENTS_LIST"
                option = False
            elif selection_menu == tournament_management_menu.MAKE_NEW_TOURNAMENT.value:
                # self.make_new_tournament()
                self.display_make_new_tournament_menu()
                # self.option_selected = "MAKE_NEW_TOURNAMENT"
                option = False
            elif selection_menu == tournament_management_menu.START_TOURNAMENT.value:
                self.start_tournament()
                self.option_selected = ""
                option = False
            elif selection_menu == tournament_management_menu.TOURNAMENT_DATA_UPDATE.value:
                self.tournament_data_update()
                self.option_selected = ""
                option = False
            elif selection_menu == tournament_management_menu.PREVIOUS_MENU.value:
                self.display_main_menu()
                option = False
            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True
        print("valeur de menu_option du ADD PLAYERS: ", self.option_selected)
        # return self.option_selected

    def display_players_management_menu(self):
        player_management_menu = PlayerManagementMenu
        player_management_options = {
            1: "Liste de joueurs",
            2: "Ajouter un joueur",
            3: "Mettre à jour les données d'un joueur",
            4: "Revenir au menu précédent"
        }
        print("\n**** GESTION DE JOUEURS ****")
        for key in player_management_options.keys():
            print(f'{key}) {player_management_options[key]}')

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            if selection_menu == player_management_menu.PLAYERS_LIST.value:
                # self.display_players_list()
                self.option_selected = "PLAYERS_LIST"
                option = False
            elif selection_menu == player_management_menu.ENTER_NEW_PLAYER.value:
                self.option_selected = "ENTER_NEW_PLAYER"
                option = False
            elif selection_menu == player_management_menu.PLAYER_DATA_UPDATE.value:
                # self.player_data_menu()
                self.option_selected = "PLAYER_DATA_UPDATE"
                option = False
            elif selection_menu == player_management_menu.PREVIOUS_MENU.value:
                self.display_main_menu()
                option = False
            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True
        print("valeur de menu_option du ADD PLAYERS: ", self.option_selected)
        # return self.option_selected

    def display_save_data_menu(self):
        print("display_save_data_menu")
        save_data_menu = SaveData
        save_data_menu_options = {
            1: "Sauvegarder les données",
            2: "Charger les données",
            3: "Revenir au menu précédent"
        }
        print("\n**** SAUVEGARDER/CHARGER LES DONNÉES ****")
        for key in save_data_menu_options.keys():
            print(f'{key}) {save_data_menu_options[key]}')

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            if selection_menu == save_data_menu.SAVE_DATA.value:
                # self.start_tournament()
                self.option_selected = "SAVE_DATA"
                option = False
            elif selection_menu == save_data_menu.LOAD_DATA.value:
                # self.display_main_menu()
                self.option_selected = "LOAD_DATA"
                option = False
            elif selection_menu == save_data_menu.PREVIOUS_MENU.value:
                self.display_main_menu()
                option = False
            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True

    def display_make_tournament_menu(self):
        new_tournament_menu = NewTournamentMenu
        new_tournament_menu_options = {
            1: "Créer un tournoi",
            2: "Revenir au menu précédent"
        }
        print("\n**** CRÉER UN TOURNOI ****")
        for key in new_tournament_menu_options.keys():
            print(f'{key}) {new_tournament_menu_options[key]}')

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            if selection_menu == new_tournament_menu.ENTER_NEW_TOURNAMENT.value:
                # self.enter_new_tournament()
                self.option_selected = "make_tournament"
                option = False
            elif selection_menu == new_tournament_menu.PREVIOUS_MENU.value:
                self.display_main_menu()
                option = False
            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True
        print("valeur de menu_option du star tournament: ", self.option_selected)

    def display_modify_tournament_menu(self):
        # tournaments = tournaments_list
        modify_tournament_menu = ModifyTournamentMenu
        modify_tournament_menu_options = {
            1: "Choisir un tournoi existant",
            2: "Revenir au menu précédent"
        }
        print("\n**** MODIFIER LES COORDONNÉES D'UN TOURNOI ****")
        for key in modify_tournament_menu_options.keys():
            print(f'{key}) {modify_tournament_menu_options[key]}')

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            if selection_menu == modify_tournament_menu.MODIFY_TOURNAMENT.value:
                # self.modify_tournament()
                self.option_selected = "modify_tournament"
                # self.display_tournaments_list()
                option = False
            elif selection_menu == modify_tournament_menu.PREVIOUS_MENU.value:
                self.display_main_menu()
                option = False
            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True

    def display_tournaments_list(self, tournaments):
        tournaments = tournaments
        print("\n** Liste de tournois **")
        for index, tournament in enumerate(tournaments, start=1):
            print(f'{index}) {tournament.name}')

        # selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
        # tournament_selected = tournaments[selection_menu-1]
        # return tournament_selected

    def display_start_tournament_menu(self):
        start_tournament_menu = StartTournamentMenu
        start_tournament_menu_options = {
            1: "Sélectionner un tournoi existant",
            2: "Revenir au menu précédent"
        }
        print("\n**** INITIER UN TOURNOI ****")
        for key in start_tournament_menu_options.keys():
            print(f'{key}) {start_tournament_menu_options[key]}')

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            if selection_menu == start_tournament_menu.START_TOURNAMENT.value:
                # self.start_tournament()
                self.option_selected = "start_tournament"
                option = False
            elif selection_menu == start_tournament_menu.PREVIOUS_MENU.value:
                self.display_main_menu()
                option = False
            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True

    def display_new_player_menu(self):
        new_player_menu = NewPlayerMenu
        new_player_menu_options = {
            1: "Ajouter un joueur",
            2: "Revenir au menu précédent"
        }
        print("\n**** AJOUTER UN JOUEUR ****")
        for key in new_player_menu_options.keys():
            print(f'{key}) {new_player_menu_options[key]}')

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            if selection_menu == new_player_menu.ENTER_NEW_PLAYER.value:
                # self.enter_new_player()
                self.option_selected = "add_players"
                option = False
            elif selection_menu == new_player_menu.PREVIOUS_MENU.value:
                self.display_main_menu()
                option = False
            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True
        print("valeur de menu_option du ADD PLAYERS: ", self.option_selected)
        # return self.option_selected

    def display_update_players_info(self):
        update_player_info_menu = ModifyPlayerInfoMenu
        update_player_info_menu_options = {
            1: "Mettre à jour les coordonnées d'un joueur",
            2: "Revenir au menu précédent"
        }
        print("\n**** METTRE A JOUR LES COORDONNÉES D'UN JOUEUR ****")
        for key in update_player_info_menu_options.keys():
            print(f'{key}) {update_player_info_menu_options[key]}')

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            if selection_menu == update_player_info_menu.UPDATE_PLAYER_INFO.value:
                # self.update_player_info()
                self.option_selected = "UPDATE_PLAYER_INFO"
                option = False
            elif selection_menu == update_player_info_menu.PREVIOUS_MENU.value:
                self.display_main_menu()
                option = False
            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True

    def display_make_reports_menu(self):
        report_menu = ReportMenu
        report_menu_options = {
            1: "Liste de tous les joueurs",
            2: "Liste des joueurs d'un tournoi",
            3: "Liste de tous les tournois",
            4: "Liste de tous les tours d'un tournoi",
            5: "Liste de tous les matchs d'un tournoi",
            6: "Revenir au menu précédent"
        }
        print("\n**** CRÉATION DE RAPPORTS ****")
        for key in report_menu_options.keys():
            print(f'{key}) {report_menu_options[key]}')

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            if selection_menu == report_menu.PLAYERS_REPORT.value:
                # self.make_players_report()
                # self.option_selected = "PLAYERS_REPORT"
                self.display_all_players_menu()
                option = False
            elif selection_menu == report_menu.PLAYERS_TOURNAMENT_REPORT.value:
                # self.make_players_by_tournament_report()
                # self.display_players_by_tournament_menu()
                self.option_selected = "PLAYERS_TOURNAMENT_REPORT"
                option = False
            elif selection_menu == report_menu.TOURNAMENTS_REPORT.value:
                self.make_tournament_report()
                option = False
            elif selection_menu == report_menu.ROUNDS_REPORT.value:
                self.make_rounds_report()
                option = False
            elif selection_menu == report_menu.MATCHS_REPORT.value:
                self.make_matchs_report()
                option = False
            elif selection_menu == report_menu.PREVIOUS_MENU.value:
                self.display_main_menu()
                option = False
            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True

    def display_all_players_menu(self):
        all_players_report_menu = AllPlayersReportMenu
        all_players_report_menu_options = {
            1: "Liste par ordre alphabétique",
            2: "Liste par classement",
            3: "Revenir au menu précédent"
        }
        print("\n**** RAPPORTS DE JOUEURS ****")
        for key in all_players_report_menu_options.keys():
            print(f'{key}) {all_players_report_menu_options[key]}')

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            if selection_menu == all_players_report_menu.ALPHABETICAL.value:
                # self.make_players_by_tournament_report()
                self.option_selected = "ALPHABETICAL"
                option = False
            elif selection_menu == all_players_report_menu.RANKING.value:
                # self.make_tournament_report()
                self.option_selected = "RANKING"
                option = False
            elif selection_menu == all_players_report_menu.PREVIOUS_MENU.value:
                self.display_make_reports_menu()
                option = False
            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True

    def display_players_by_tournament_menu(self):
        all_players_by_tournament_report_menu = PlayersByTournamentReportMenu
        all_players_by_tournament_report_menu_options = {
            1: "Liste par ordre alphabétique",
            2: "Liste par classement"
        }
        print("\n**** RAPPORTS DE JOUEURS ****")
        for key in all_players_by_tournament_report_menu_options.keys():
            print(f'{key}) {all_players_by_tournament_report_menu_options[key]}')

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            if selection_menu == all_players_by_tournament_report_menu.ALPHABETICAL_BY_TOURNAMENT.value:
                # self.make_players_by_tournament_report()
                self.option_selected = "ALPHABETICAL_BY_TOURNAMENT"
                option = False
            elif selection_menu == all_players_by_tournament_report_menu.RANKING_BY_TOURNAMENT.value:
                # self.make_tournament_report()
                self.option_selected = "RANKING_BY_TOURNAMENT"
                option = False
            # elif selection_menu == all_players_by_tournament_report_menu.PREVIOUS_MENU.value:
            #     self.display_make_reports_menu()
            #     option = False
            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True

        return self.option_selected
    ##### TODO DELETE UP TO HERE

    def enter_tournament_selection(self, tournaments):
        self.display_tournaments_list(tournaments)
        number_of_tournament_list = []
        # print("tournaments : ", tournaments)
        # print("tournaments[0] : ", tournaments[0])
        # print("tournaments[0].name : ", tournaments[0].name)
        for number_of_tournament in range(len(tournaments)):
            number_of_tournament_list.append(number_of_tournament + 1)

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)

            if selection_menu in number_of_tournament_list:
                print("number_of_tournament dans le if : ", number_of_tournament_list)
                option = False
                tournament = tournaments[selection_menu - 1]
                return tournament

            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True

    @staticmethod
    def display_players_list(players: Dict):
        # player_parameter = 0
        print("players : ", players)
        print("\n** Liste de joueurs **")
        for key, player in players.items():
            print(f'{key} - {player.first_name} {player.last_name}')

    def update_player_info(self, players: Dict):
        players = players
        self.display_players_list(players)
        selection_menu = input_with_constraint("\nChoisissez un joueur : ", parse_fn=parse_positive_int)
        for key, player in players.items():
            if key == selection_menu:
                new_info_player = self.enter_new_player()
                players.update({key: new_info_player})

        return players

    def display_make_new_tournament_menu(self):
        make_new_tournament_menu = MakeNewTournamentMenu
        make_new_tournament_menu_options = {
            1: "Ajouter les joueurs depuis la base de données",
            2: "Ajouter des nouveaux joueurs",
            3: "Revenir au menu précédent"
        }
        print("\n** Ajout de joueurs **")
        for key in make_new_tournament_menu_options.keys():
            print(f'{key}) {make_new_tournament_menu_options[key]}')

        option = True
        while option:
            selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            if selection_menu == make_new_tournament_menu.PLAYERS_FROM_DATA_BASE.value:
                # self.enter_new_player()
                self.option_selected = "PLAYERS_FROM_DATA_BASE"
                option = False
            elif selection_menu == make_new_tournament_menu.PLAYERS_FROM_TYPING.value:
                # self.display_main_menu()
                self.option_selected = "PLAYERS_FROM_TYPING"
                option = False
            elif selection_menu == make_new_tournament_menu.PREVIOUS_MENU.value:
                self.display_tournament_management_menu()
                option = False
            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True
        print("valeur de menu_option du ADD PLAYERS: ", self.option_selected)
        # return self.option_selected

    @staticmethod
    def enter_tournament_info(players):
        # tournaments = tournaments
        # self.display_tournaments_list(tournaments)
        # selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)

        tournament = Tournament(
            name=input('Nom du tournoi : '),
            place=input('Lieu du tournoi : '),
            time_control=input_with_constraint('Contrôle du temps (bullet/blitz/quick play) : ',
                                               parse_fn=TimeControlKind),
            description=input('Description : '),
            players=players
        )
        return tournament

    # @staticmethod
    def enter_new_players_in_tournament(self, player_selection, all_players_listed, players_id_set):
        option = True
        selection_menu = 0

        while option:
            selection_menu = input_with_constraint(
                f"\nChoisissez l'identifiant du joueur {player_selection} : ", parse_fn=parse_positive_int)
            if selection_menu > all_players_listed or selection_menu in players_id_set:
                print("-- Choisissez un autre identifiant --")
                option = True
            else:
                option = False

        return selection_menu

    def player_data_menu(self):
        print("player_data_menu")

    def modify_tournament(self):
        pass

    # def add_players(self) -> List[Player]:
    #     """Joueurs ajoutés + points de départ égal à 0 """
    #     player_with_score = PlayerScore
    #     player_list = []
    #     players_with_score = []
    #     for players_number in range(DEFAULT_PLAYERS_NUMBER):
    #         player = self.enter_new_player()
    #         player_list.append(player)
    #         player_with_score = (player, SCORE_INIT)
    #         players_with_score.append(player_with_score)
    #         print("Valeur de player : ", player_list)
    #         print("Valeur de player avec score : ", players_with_score)
    #     return players_with_score

    def display_add_players_options(self):
        pass

    @staticmethod
    def enter_player_info():  # -> Player:
        # How to parse/validate?
        # first_name = input('Prénom : ')
        # if first_name == "":
        #     first_name = Player.first_name
        # else:
        #     first_name = first_name
        # print("first_name : ", first_name)

        player = Player(
            first_name=input('Prénom : '),
            last_name=input('Nom : '),
            date_of_birth=input_with_constraint('Date de naissance (aaaa-mm-dd) : ', parse_fn=date.fromisoformat),
            sex=input_with_constraint('Genre (h/f) : ', parse_fn=Sex).value,
            ranking=input_with_constraint('Classement : ', parse_fn=parse_positive_int)
        )
        # score = MatchResult
        # player_with_score = [player, score.LOSS]
        # print("nouveau joueur : ", player_with_score)
        return player

    # def display_players(self, players: List[Player]):
    #     for idx, player in enumerate(players, start=1):
    #         print(f'{idx} -- {player}')

    # def format_players_json(self, players: List[Player]) -> str:
    #     json_str = "["
    #     for player in players:
    #         json_str += player.as_json()
    #         json_str += ","
    #     json_str += "]"
    #     return json_str

    def print_players_report(self, players: List[Player]):
        # in controller.print_all_players():
        #     self.view.print_players_report(self.players)

        # in controller.print_tournament_players():
        #     self.view.print_players_report(self.current_tournament.players)
        pass

    def make_players_report(self, row_lists, report, file_name):
        head_list = ["identifiant", "prenom", "nom", "date de naissance", "sexe", "classement"]
        name_of_file = "rapports/liste de joueurs.csv"

        if report == "all_players_name_order":
            # nom_du_fichier = 'rapports/liste de joueurs par ordre alphabetique.csv'
            name_of_file = 'rapports/' + file_name + '.csv'
        elif report == "all_players_ranking_order":
            # nom_du_fichier = 'rapports/liste de joueurs par classement.csv'
            name_of_file = 'rapports/' + file_name + '.csv'
        elif report == "players_in_tournament_by_alphabetical_order":
            # nom_du_fichier = 'rapports/liste de joueurs par ordre alphabetique selon tournoi.csv'
            name_of_file = 'rapports/' + file_name + '.csv'
        elif report == "players_in_tournament_by_ranking_order":
            # nom_du_fichier = 'rapports/liste de joueurs par classement selon tournoi.csv'
            name_of_file = 'rapports/' + file_name + '.csv'

        with open(name_of_file, 'w', encoding='utf8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(head_list)
            writer.writerows(row_lists)

    def make_players_by_tournament_report(self):
        pass

    def make_tournament_report(self):
        pass

    def make_rounds_report(self):
        pass

    def make_matchs_report(self):
        pass
