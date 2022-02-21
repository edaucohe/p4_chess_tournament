from controllers.controllers_file import Controller


def main():
    """Récupérer info de deux joueurs"""
    players_added = Controller()
    players_added.add_players()
    players_added.sent_players_to_screen()


if __name__ == "__main__":
    main()
