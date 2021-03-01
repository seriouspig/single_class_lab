class Team():
    def __init__(self, name, list_of_players, coach, points = 0):
        self.name = name
        self.players = list_of_players
        self.coach = coach
        self.points = points

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_check):
        if player_check in self.players:
            return True
        else:
            return False

    def play_game(self, win):
        if win == True:
            self.points += 3
        else:
            self.points = self.points

    