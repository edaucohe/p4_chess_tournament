import csv
from datetime import date
from typing import Any, Callable, List, Dict, Optional

from chess.models import Player, Sex, Tournament, TimeControlKind, Round


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


def only_one_input_with_constraint(desc: str, parse_fn: Callable[[str], Any]):
    while True:
        input_value = input(desc)
        if input_value == "":
            return None
        else:
            try:
                return parse_fn(input_value)
            except ValueError:
                print("Merci de respecter le bon format")
            except AssertionError:
                print("La valeur doit être un numéro positif")


class TerminalView:
    @staticmethod
    def display_menu(name: str, choices: Dict[int, str]):
        print(f'\n**{name}**')
        for choice_index, choice_name in choices.items():
            print(f'{choice_index} - {choice_name}')

    @staticmethod
    def input_for_menu(choices: Dict[int, str], header: Optional[str] = None):
        if header is not None:
            print(header)

        user_input = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
        is_input_valid = user_input in choices

        while not is_input_valid:
            user_input = input_with_constraint("\nChoisissez une option : ", parse_fn=parse_positive_int)
            is_input_valid = user_input in choices

        return user_input

    @staticmethod
    def display_a_simple_message(message):
        print(message)

    @staticmethod
    def enter_tournament_info(players: Optional[Dict[int, Player]] = None):
        tournament = Tournament(
            name=input('Nom du tournoi : '),
            place=input('Lieu du tournoi : '),
            time_control=input_with_constraint('Contrôle du temps (bullet/blitz/quick play) : ',
                                               parse_fn=TimeControlKind),
            description=input('Description : '),
            round_count=input_with_constraint('Nombre de round : ', parse_fn=parse_positive_int),
            players=players or {},
            scores={}
        )
        return tournament

    @staticmethod
    def enter_tournament_update_info(existing_tournament: Tournament):
        # TODO
        tournament = Tournament(
            name=input('Nom du tournoi : '),
            place=input('Lieu du tournoi : '),
            time_control=input_with_constraint('Contrôle du temps (bullet/blitz/quick play) : ',
                                               parse_fn=TimeControlKind),
            description=input('Description : '),
            round_count=input_with_constraint('Nombre de round : ', parse_fn=parse_positive_int),
            players=players or {},
            scores={}
        )
        return tournament

    @staticmethod
    def enter_player_info():  # -> Player:
        player = Player(
            first_name=input('Prénom : '),
            last_name=input('Nom : '),
            date_of_birth=input_with_constraint('Date de naissance (aaaa-mm-dd) : ', parse_fn=date.fromisoformat),
            sex=input_with_constraint('Genre (h/f) : ', parse_fn=Sex).value,
            ranking=input_with_constraint('Classement : ', parse_fn=parse_positive_int)
        )
        return player

    @staticmethod
    def update_player_info(first_name, last_name, date_of_birth, sex, ranking):  # -> Player:
        player = Player(
            first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, sex=sex, ranking=ranking)
        return player

    @staticmethod
    def enter_first_name_data():
        return input("Prénom : ")

    @staticmethod
    def enter_last_name_data():
        return input("Nom : ")

    @staticmethod
    def enter_birth_data():
        return only_one_input_with_constraint('Date de naissance (aaaa-mm-dd) : ', parse_fn=date.fromisoformat)

    @staticmethod
    def enter_sex_data():
        sex = only_one_input_with_constraint('Genre (h/f) : ', parse_fn=Sex)
        return sex.value

    @staticmethod
    def enter_ranking_data():
        return only_one_input_with_constraint('Classement : ', parse_fn=parse_positive_int)

    # @staticmethod
    # def enter_one_player_info(choice):
    #     if choice == "":
    #         player = Player(
    #             first_name=Player.first_name,
    #             last_name=input('Nom : '),
    #             date_of_birth=input_with_constraint('Date de naissance (aaaa-mm-dd) : ', parse_fn=date.fromisoformat),
    #             sex=input_with_constraint('Genre (h/f) : ', parse_fn=Sex).value,
    #             ranking=input_with_constraint('Classement : ', parse_fn=parse_positive_int)
    #         )
    #
    #     return player

    @staticmethod
    def enter_new_round(round_name):
        return Round(matches=[], name=round_name)

    @staticmethod
    def enter_round_info(end_date):
        round_info = Round(matches=[], name=input('Nom du round : '), end=end_date)
        return round_info

    @staticmethod
    def enter_round_match(match, round_name):
        return Round(matches=match, name=round_name)

    @staticmethod
    def round_finished():
        return Round.close

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

    @staticmethod
    def make_players_report(row_lists, report, file_name):
        head_list = ["identifiant", "prenom", "nom", "date de naissance", "sexe", "classement"]
        name_of_file = "rapports/liste de joueurs.csv"

        if report == "all_players_name_order":
            # nom_du_fichier = 'rapports/liste de joueurs par ordre alphabétique.csv'
            name_of_file = 'rapports/' + file_name + '.csv'
        elif report == "all_players_ranking_order":
            # nom_du_fichier = 'rapports/liste de joueurs par classement.csv'
            name_of_file = 'rapports/' + file_name + '.csv'
        elif report == "players_in_tournament_by_alphabetical_order":
            # nom_du_fichier = 'rapports/liste de joueurs par ordre alphabétique selon tournoi.csv'
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

    @staticmethod
    def make_common_report_for_rounds_and_matches(name: str, choices: Dict):
        print(f'\n**{name}**')
        for choice_index, choice_name in choices.items():
            print(f'{choice_index} {choice_name}')

    def make_matchs_report(self):
        pass
