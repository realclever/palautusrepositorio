class PlayerStats:

    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        print(f'Players from {nationality:2}\n')

        filter = [player for player in self.reader.get_players() if player.nationality == nationality]
        sortedlist = sorted(filter, key=lambda player : player.points, reverse=True)

        return sortedlist