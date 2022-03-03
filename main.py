from typing import Dict, List

from chess.controller import Controller
from chess.models import Player, MatchResult


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


def main():
    # TODO delete me once the database is implemented
    players: Dict[int, List] = players_added_for_test()
    print("joueurs du tournois : ", players)
    # TODO delete up to here

    # players = db.load_players()

    controller = Controller(players=players)
    controller.run_chess_script()

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
