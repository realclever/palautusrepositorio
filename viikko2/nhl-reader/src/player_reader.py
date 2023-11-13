import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        players_file = requests.get(self._url).json()
        players = []   

        for line in players_file:
            player = Player(line)
            players.append(player)

        return players