from datetime import date
from typing import Any, Callable, Dict, Optional

from chess.models import Player, Sex, Tournament, TimeControlKind, Round


def input_with_constraint(desc: str, parse_fn: Callable[[str], Any]):
    while True:
        try:
            input_value = input(desc)
            return parse_fn(input_value)
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
            players=players or {},
            scores={}
        )
        return tournament

    @staticmethod
    def enter_tournament_name():
        return input("Nom : ")

    @staticmethod
    def enter_tournament_place():
        return input("Place : ")

    @staticmethod
    def enter_tournament_time_control():
        return only_one_input_with_constraint(
            'Contrôle du temps (bullet/blitz/quick play) : ', parse_fn=TimeControlKind)

    @staticmethod
    def enter_tournament_description():
        return input("Description : ")

    @staticmethod
    def enter_player_info():
        player = Player(
            first_name=input('Prénom : '),
            last_name=input('Nom : '),
            date_of_birth=input_with_constraint('Date de naissance (aaaa-mm-dd) : ', parse_fn=date.fromisoformat),
            sex=input_with_constraint('Genre (h/f) : ', parse_fn=Sex),
            ranking=input_with_constraint('Classement : ', parse_fn=parse_positive_int)
        )
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
        return only_one_input_with_constraint('Genre (h/f) : ', parse_fn=Sex)

    @staticmethod
    def enter_ranking_data():
        return only_one_input_with_constraint('Classement : ', parse_fn=parse_positive_int)

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
    def make_common_report_for_rounds_and_matches(name: str, choices: Dict):
        print(f'\n**{name}**')
        for choice_index, choice_name in choices.items():
            print(f'{choice_index} {choice_name}')
