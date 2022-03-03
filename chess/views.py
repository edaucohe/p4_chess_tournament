from datetime import date
from typing import Any, Callable, List
# from dataclasses import dataclass, asdict  # , field

from chess.models import Player, Sex, MainMenu, ReportMenu, NewPlayerMenu, NewTournamentMenu, ModifyTournamentMenu, \
    ModifyPlayerInfoMenu, StartTournamentMenu, MENU_OPTION, Tournament, TimeControlKind, DEFAULT_PLAYERS_NUMBER, \
    PlayerScore, SCORE_INIT, PlayerManagementMenu, TournamentManagementMenu, SaveData


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

            print("valeur de menu_option du MAIN WHILE : ", self.option_selected)
        print("valeur de menu_option du MAIN HORS WHILE : ", self.option_selected)
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
                self.display_tournaments_list()
                option = False
            elif selection_menu == tournament_management_menu.MAKE_NEW_TOURNAMENT.value:
                self.make_new_tournament()
                self.option_selected = ""
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
                self.enter_new_player()
                self.option_selected = "ENTER_NEW_PLAYER"
                option = False
            elif selection_menu == player_management_menu.PLAYER_DATA_UPDATE.value:
                self.player_data_menu()
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

    def display_tournaments_list(self, tournaments_list):
        tournaments = tournaments_list
        print("\n** Choisissez un tournoi **")
        for index, tournament in enumerate(tournaments, start=1):
            print(f'{index}) {tournament.name}')

        selection_menu = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
        tournament_selected = tournaments[selection_menu-1]
        return tournament_selected

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
            if selection_menu == update_player_info_menu.MODIFY_PLAYER_INFO.value:
                self.update_player_info()
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
            1: "Liste de tous les joueurs (a/c)",
            2: "Liste des joueurs d'un tournoi (a/c)",
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
            if selection_menu == report_menu.PLAYERS_LIST.value:
                self.make_players_report()
                option = False
            elif selection_menu == report_menu.PLAYERS_TOURNAMENT_LIST.value:
                self.make_players_by_tournament_report()
                option = False
            elif selection_menu == report_menu.TOURNAMENT_LIST.value:
                self.make_tournament_report()
                option = False
            elif selection_menu == report_menu.ROUNDS_LIST.value:
                self.make_rounds_report()
                option = False
            elif selection_menu == report_menu.MATCHS_LIST.value:
                self.make_matchs_report()
                option = False
            elif selection_menu == report_menu.PREVIOUS_MENU.value:
                self.display_main_menu()
                option = False
            else:
                print("-- Choisissez une option parmi les proposées --")
                option = True

    def display_players_list(self, list_of_players):
        print("display_players_list")
        print(list_of_players)

    def enter_new_tournament(self):
        tournament = Tournament(
            name=input('Nom du tournoi : '),
            place=input('Lieu du tournoi : '),
            time_control=input_with_constraint('Contrôle du temps (bullet/blitz/quick play) : ',
                                               parse_fn=TimeControlKind),
            description=input('Description : '),
            players=self.add_players()
        )
        return tournament

    def player_data_menu(self):
        print("player_data_menu")

    def modify_tournament(self):
        pass

    def update_player_info(self):
        pass

    def add_players(self) -> List[Player]:
        """Joueurs ajoutés + points de départ égal à 0 """
        player_with_score = PlayerScore
        player_list = []
        players_with_score = []
        for players_number in range(DEFAULT_PLAYERS_NUMBER):
            player = self.enter_new_player()
            player_list.append(player)
            player_with_score = (player, SCORE_INIT)
            players_with_score.append(player_with_score)
            print("Valeur de player : ", player_list)
            print("Valeur de player avec score : ", players_with_score)
        return players_with_score

    def enter_new_player(self) -> Player:
        # How to parse/validate?
        player = Player(
            first_name=input('Prénom : '),
            last_name=input('Nom : '),
            date_of_birth=input_with_constraint('Date de naissance (aaaa-mm-dd) : ', parse_fn=date.fromisoformat),
            sex=input_with_constraint('Genre (h/f) : ', parse_fn=Sex),
            ranking=input_with_constraint('Classement : ', parse_fn=parse_positive_int)
        )

        return player

    def display_players(self, players: List[Player]):
        for idx, player in enumerate(players, start=1):
            print(f'{idx} -- {player}')

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

    def make_players_report(self):
        pass

    def make_players_by_tournament_report(self):
        pass

    def make_tournament_report(self):
        pass

    def make_rounds_report(self):
        pass

    def make_matchs_report(self):
        pass