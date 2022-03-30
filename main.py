from datetime import date, datetime
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

    # players_with_index = {index+1: Player for index in range(len(Player))}
    players_with_id = {index + 1: players[index] for index in range(len(players))}
    return players_with_id


def tournaments_added_for_test(players, round_for_starting):
    tournaments_list = []
    scores = {
        players.get(1): 0,
        players.get(2): 0,
        players.get(3): 0,
        players.get(4): 0,
        players.get(5): 0,
        players.get(6): 0,
        players.get(7): 0,
        players.get(8): 0
    }
    tournaments = [
        {
            "name": "Master chess tournament Dubai 2022",
            "place": "Dubai",
            "time_control": TimeControlKind.BLITZ,
            "description": "Tous les meilleurs joueurs du monde",
            "players": players,
            'scores': scores,
            "start": date.today(),
            "round_count": MAX_TURNS_COUNT,
            "rounds": [round_for_starting[0]]
        },
        {
            "name": "National chess tournament Paris 2022",
            "place": "Paris",
            "time_control": TimeControlKind.QUICK_PLAY,
            "description": "Les meilleurs joueurs de la France",
            "players": players,
            'scores': scores,
            "start": date.today(),
            "round_count": MAX_TURNS_COUNT,
            "rounds": [round_for_starting[1]]
        }
    ]
    for tournament in tournaments:
        tournament = Tournament(**tournament)
        tournaments_list.append(tournament)

    tournament_with_index = {index + 1: tournaments_list[index] for index in range(len(tournaments))}
    return tournament_with_index


def rounds_added_for_test():
    rounds_list = []
    round_elements = [
        {
            "matches": [],
            "name": "ROUND 1",
            "start": datetime.now(),
            "end": None
        },
        {
            "matches": [],
            "name": "ROUND 4",
            "start": datetime.now(),
            "end": datetime.now()
        }
    ]
    for round_element in round_elements:
        round_element = Round(**round_element)
        rounds_list.append(round_element)

    return rounds_list


def main():
    # TODO delete me once the database is implemented
    players: Dict[int, Player] = players_added_for_test()
    round_for_starting = rounds_added_for_test()
    print("round_for_starting : ", round_for_starting)
    tournaments = tournaments_added_for_test(players, round_for_starting)
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

    controller = Controller(players=players, tournaments=tournaments)
    controller.display_main_menu()


if __name__ == "__main__":
    main()
