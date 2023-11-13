class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.points = dict['goals']+dict['assists']

    def __str__(self):
        return f'{self.name:20}{self.team:4}{self.goals:3} + {self.assists:2} = {self.points}'