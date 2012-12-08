
points_translation=["0","15","30","40","AD"]

class Match():

    def __init__(self):
        self.points = {"Player1":0,"Player2":0}
        self.games = {"Player1":0,"Player2":0}

    def scores(self,player):
        self.points[player] += 1
        if (self.points["Player2"] == self.points["Player2"] == 4):
            self.points["Player1"] -= 1
            self.points["Player2"] -= 1
        elif (self.points["Player2"] + self.points["Player1"] > 7):
            self.gameWon(player)
        elif (self.points[player] == 4 and (self.points["Player2"] + self.points["Player1"] != 7)):
            self.gameWon(player)

    def gameWon(self,player):
        self.games[player] += 1
        self.points["Player1"] = 0
        self.points["Player2"] = 0

    def endMatch(self):
        return True

    def getScore(self,player):
        return points_translation[self.points[player]]

    def getGamesScore(self):
        return str(self.games["Player1"]) + "-" + str(self.games["Player2"])
