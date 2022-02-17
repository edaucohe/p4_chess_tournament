from dataclasses import dataclass
from views.views_file import InfoPlayers


@dataclass
class Controller:
    players_to_add = InfoPlayers()

    def add_players(self):
        player_added = self.players_to_add.get_players_info()
        return player_added
