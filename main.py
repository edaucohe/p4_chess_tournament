from datetime import date, datetime
from typing import Dict

from chess.controller import Controller
from chess.models import Player, Tournament, Round, MAX_TURNS_COUNT, DEFAULT_TURN_COUNT, TEST_TURN_COUNT


def players_added_for_test() -> Dict[int, Player]:
    players_list = []
    players = [
        {
            "first_name": "John",
            "last_name": "OLLE",
            "date_of_birth": "1980-10-10",
            "sex": "h",
            "ranking": 1660
        },
        {
            "first_name": "Marie",
            "last_name": "THIBAUD",
            "date_of_birth": "1985-01-17",
            "sex": "f",
            "ranking": 1695
        },
        {
            "first_name": "Jeanne",
            "last_name": "BOYER",
            "date_of_birth": "1986-07-27",
            "sex": "h",
            "ranking": 1700
        },
        {
            "first_name": "Pierre",
            "last_name": "LUC",
            "date_of_birth": "1981-04-04",
            "sex": "h",
            "ranking": 1684
        },
        {
            "first_name": "David",
            "last_name": "MOLLY",
            "date_of_birth": "1975-12-22",
            "sex": "h",
            "ranking": 1715
        },
        {
            "first_name": "Marc",
            "last_name": "MONTY",
            "date_of_birth": "1980-08-11",
            "sex": "f",
            "ranking": 1707
        },
        {
            "first_name": "Sophie",
            "last_name": "LEON",
            "date_of_birth": "1978-11-08",
            "sex": "f",
            "ranking": 1677
        },
        {
            "first_name": "Claire",
            "last_name": "LAMANT",
            "date_of_birth": "1982-06-14",
            "sex": "f",
            "ranking": 1653
        }
    ]
    # score = MatchResult
    for player in players:
        player = Player(**player)
        players_list.append(player)

    # players_with_index = {index+1: Player for index in range(len(Player))}
    players_with_id = {index + 1: players_list[index] for index in range(len(players))}
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
            "time_control": "bullet",
            "description": "Tous les meilleurs joueurs du monde",
            "players": players,
            'scores': scores,
            "start": date.today,
            "round_count": DEFAULT_TURN_COUNT,
            "rounds": [round_for_starting[0]]
        },
        {
            "name": "National chess tournament Paris 2022",
            "place": "Paris",
            "time_control": "bullet",
            "description": "Les meilleurs joueurs de la France",
            "players": players,
            'scores': scores,
            "start": date.today,
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
            "name": "Round " + str(DEFAULT_TURN_COUNT),
            "start": datetime.now(),
            "end": None
        },
        {
            "matches": [],
            "name": "Round " + str(MAX_TURNS_COUNT),
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

    # """Récupérer info des joueurs"""
    # players_added.add_players()
    #
    # """Trier les joueurs selon leurs classements"""
    # players_added.classify_by_ranking()
    #
    # """Afficher les joueurs"""
    # players_added.send_players_to_screen()

    # players_added.assign_points()
    # players_added.groups_number()


if __name__ == "__main__":
    main()
