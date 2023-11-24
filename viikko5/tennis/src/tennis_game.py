class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

        self.score = ""
        self.temp_score = 0
        self.round = 1

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points += self.round
        else:
            self.player2_points += self.round

    def player_score(self, score, temp_score):
        if temp_score == 0:
            return score + 'Love'
        elif temp_score == 1:
            return score + 'Fifteen'
        elif temp_score == 2:
            return score + 'Thirty'
        else:
            return score + 'Forty'

    def tie_score(self):
        if self.player1_points == 0:
            return 'Love-All'
        elif self.player1_points == 1:
            return 'Fifteen-All'
        elif self.player1_points == 2:
            return 'Thirty-All'
        else:
            return 'Deuce'

    def advantage_score(self):
        result = self.player1_points - self.player2_points

        if result == 1:
            return 'Advantage player1'
        elif result == -1:
            return 'Advantage player2'
        elif result >= 2:
            return 'Win for player1'
        else:
            return 'Win for player2'

    def return_score(self):
        for i in range(1, 3):
            if i == 1:
                self.temp_score = self.player1_points
            else:
                self.score += "-"
                self.temp_score = self.player2_points

            self.score = self.player_score(self.score, self.temp_score)

        return self.score        

    def get_score(self):
        if self.player1_points == self.player2_points:
           return self.tie_score()
        
        elif self.player1_points >= 4 or self.player2_points >= 4:
            return self.advantage_score()
        
        return self.return_score()