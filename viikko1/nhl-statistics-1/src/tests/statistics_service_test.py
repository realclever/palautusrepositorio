import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_find_single_player_by_name(self):
        player = self.stats.search("Gretzky") 

        self.assertAlmostEqual(player.name, "Gretzky")   

    def test_find_unlisted_player_by_name(self):
        player = self.stats.search("Gretky")    

        self.assertIsNone(player)

    def test_return_correct_number_of_players(self):
        players = len(self.stats._players)
        list = len(PlayerReaderStub().get_players())

        self.assertAlmostEqual(players, list)     

    def test_find_players_by_team(self):
        list = self.stats.team("EDM")
        player_names = [p.name for p in list]
        
        self.assertListEqual(player_names, ["Semenko", "Kurri", "Gretzky"])

    def test_top_players_by_points(self):
        players = self.stats.top(2, SortBy.POINTS)
        player_names = [p.name for p in players]

        self.assertListEqual(player_names, ["Gretzky", "Lemieux", "Yzerman"])
        
    def test_top_players_by_goals(self):
        players = self.stats.top(2, SortBy.GOALS)
        player_names = [p.name for p in players]

        self.assertListEqual(player_names, ["Lemieux", "Yzerman", "Kurri"])
       
    def test_top_players_by_assists(self):
        players = self.stats.top(2, SortBy.ASSISTS)
        player_names = [p.name for p in players]

        self.assertListEqual(player_names, ["Gretzky", "Yzerman", "Lemieux"])
    