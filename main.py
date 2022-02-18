from controllers.controllers_file import Controller, Test


def main():
    """Récupérer info d'un seul joueur"""
    players_added = Controller()
    info_player = players_added.add_players()
    print("---- joueur 1 ----")
    print(info_player)

    x_data = 5
    y_data = 6
    data_test = Test()
    data_test.somme(x_data, y_data)
    print("valeur de la somme : ", data_test.z)


if __name__ == "__main__":
    main()
