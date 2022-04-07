from datetime import date
from typing import Dict, List

from chess.controller import Controller
from chess.models import Player, Sex, Tournament, Round, MAX_TURNS_COUNT, TimeControlKind


def players_added_for_test() -> Dict[int, Player]:
    players: List[Player] = [
        Player("John", "OLLE", date.fromisoformat("1980-10-10"), Sex.MALE, 1660),
        Player("Marie", "THIBAUD", date.fromisoformat("1980-10-10"), Sex.FEMALE, 1695),
        Player("Jeanne", "BOYER", date.fromisoformat("1986-07-27"), Sex.FEMALE, 1700),
        Player("Pierre", "LUC", date.fromisoformat("1981-10-10"), Sex.MALE, 1684),
        Player("David", "MOLLY", date.fromisoformat("1975-10-10"), Sex.MALE, 1715),
        Player("Marc", "MONTY", date.fromisoformat("1975-10-10"), Sex.MALE, 1706),
        Player("Sophie", "LEON", date.fromisoformat("1975-10-10"), Sex.FEMALE, 1677),
        Player("Claire", "LAMANT", date.fromisoformat("1975-10-10"), Sex.FEMALE, 1653),
    ]

    players_with_id = {index + 1: players[index] for index in range(len(players))}
    return players_with_id


def tournaments_added_for_test(players, rounds):
    scores = {
        players[1]: 0,
        players[2]: 0,
        players[3]: 0,
        players[4]: 0,
        players[5]: 0,
        players[6]: 0,
        players[7]: 0,
        players[8]: 0
    }
    tournaments = [
        Tournament("Master chess tournament Dubai 2022", "Dubai", TimeControlKind.QUICK_PLAY,
                   "Les meilleurs joueurs de la France", players, scores, date.today(), MAX_TURNS_COUNT,
                   [rounds[0]]),
        Tournament("National chess tournament Paris 2022", "Paris", TimeControlKind.BULLET,
                   "Les meilleurs joueurs de la France", players, scores, date.today(), MAX_TURNS_COUNT,
                   [rounds[1]])
    ]

    tournament_with_index = {index + 1: tournaments[index] for index in range(len(tournaments))}
    return tournament_with_index


def rounds_added_for_test():
    round_elements = [
        Round([], "ROUND 1"),
        Round([], "ROUND 4")
    ]
    return round_elements


def main():
    # TODO delete me once the database is implemented
    # players: Dict[int, Player] = players_added_for_test()
    # print("players : ", players)
    # rounds = rounds_added_for_test()
    # print("round_for_starting : ", rounds)
    # tournaments = tournaments_added_for_test(players, rounds)
    # print("joueurs du tournois : ", players)
    # print("tournois : ", tournaments)
    # list_of_numbers = [0, 1, 2, 3, 4]
    # set_number = set(list_of_numbers)
    # print("set_number : ", set_number)
    # number = int(input("tapez un numéro : "))
    # if number not in set_number:
    #     print(f"numéro {number} n'est pas dans la liste {list_of_numbers}")
    # else:
    #     print(f"numéro {number} est dans la liste {list_of_numbers}")
    # TODO delete up to here

    # players = db.load_players()

    # controller = Controller(players=players)
    controller = Controller()
    controller.display_main_menu()


if __name__ == "__main__":
    main()
