from controllers.controllers_file import Controller


def main():
    """Récupérer info de deux joueurs"""
    players_added = Controller()
    players_added.add_players()

    """Afficher les joueurs"""
    players_added.send_players_to_screen()

    """Trier les joueurs selon leurs classements"""
    players_added.classify_players()


if __name__ == "__main__":
    main()
