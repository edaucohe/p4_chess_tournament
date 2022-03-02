from chess.controller import Controller
from chess.models import Player


def new_player(idx: int) -> Player:
    return Player(...)

def main():
    # TODO delete me once the database is implemented
    players = {idx+1: new_player(idx+1) for idx in range(8)}
    # delete up to here
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




