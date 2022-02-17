from controllers.controllers_file import Controller


def main():
    """Récupérer info d'un seul joueur"""
    players_added = Controller()
    info_player = players_added.add_players()
    print("---- joueur 1 ----")
    print("Prénom : ", info_player.first_name)
    print("Nom : ", info_player.last_name)
    print("Date de naissance : ", info_player.day_of_birth)
    print("Sexe : ", info_player.sex)
    print("Classement : ", info_player.ranking)


if __name__ == "__main__":
    main()
