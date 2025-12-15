class TennisGame:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.scores = {
            self.player_1: 0,
            self.player_2: 0
        }

    def score(self):
        if self.scores[self.player_1] == self.scores[self.player_2] and self.scores[self.player_1] == 0:
            return "love-all"

        return "fifteen-love"

    def won_point(self, player):
        self.scores[player] += 1

