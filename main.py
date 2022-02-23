from controllers.controllers_file import Controller


def main():
    players_added = Controller()

    """Récupérer info des joueurs"""
    players_added.add_players()

    """Trier les joueurs selon leurs classements"""
    players_added.classify_by_ranking()

    """Afficher les joueurs"""
    players_added.send_players_to_screen()

    # players_added.assign_points()
    # players_added.groups_number()


if __name__ == "__main__":
    main()
