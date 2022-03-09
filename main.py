from datetime import date
from typing import Dict, List

from chess.controller import Controller
from chess.models import Player, MatchResult, DEFAULT_TURNS_COUNT, Tournament


def players_added_for_test() -> Dict[int, List]:
    players_with_score = []
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
    score = MatchResult
    for player in players:
        player = Player(**player)
        players_with_score.append([player, score.LOSS])

    players_with_index = {index+1: players_with_score[index] for index in range(len(players))}
    return players_with_index


def tournaments_added_for_test(players):
    tournaments_list = []
    tournaments = [
        {
            "name": "Master chess tournament Dubai 2022",
            "place": "Dubai",
            "time_control": "bullet",
            "description": "Tous les meilleurs joueurs du monde",
            "players": players,
            "start": date.today,
            "turn_count": DEFAULT_TURNS_COUNT,
            "round": []
        },
        {
            "name": "National chess tournament Paris 2022",
            "place": "Paris",
            "time_control": "bullet",
            "description": "Les meilleurs joueurs de la France",
            "players": players,
            "start": date.today,
            "turn_count": DEFAULT_TURNS_COUNT,
            "round": []
        }
    ]
    for tournament in tournaments:
        tournament = Tournament(**tournament)
        tournaments_list.append(tournament)

    # tournament_with_index = {index + 1: tournaments_list[index] for index in range(len(tournaments))}
    return tournaments_list


def main():
    # TODO delete me once the database is implemented
    players: Dict[int, List] = players_added_for_test()
    tournaments = tournaments_added_for_test(players)
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
    controller.main_menu()

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
