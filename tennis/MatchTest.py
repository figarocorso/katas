import unittest
from Match import Match

class MatchTest(unittest.TestCase):

    def setUp(self):
        self.match = Match()

    def scoreNpoints(self,player,points):
        for i in range(0, points):
            self.match.scores(player)

    def testEndMatch(self):
        self.assertEqual(True,self.match.endMatch())

    def testPlayer1Score(self):
        self.assertEqual("0",self.match.getScore("Player1"))

    def testPlayer1Scores(self):
        self.scoreNpoints("Player1",1)
        self.assertEqual("15",self.match.getScore("Player1"))

    def testPlayer1Scores(self):
        self.scoreNpoints("Player1",2)
        self.assertEqual("30",self.match.getScore("Player1"))

    def testPlayer1ScoresThreeTimes(self):
        self.scoreNpoints("Player1",3)
        self.assertEqual("40",self.match.getScore("Player1"))

    def testPlayer1ScoresFourTimes(self):
        self.scoreNpoints("Player1",4)
        self.assertEqual("0",self.match.getScore("Player1"))
        self.assertEqual("1-0",self.match.getGamesScore())

    def testPlayer2ScoresThreeTimes(self):
        self.scoreNpoints("Player1",1)
        self.scoreNpoints("Player2",1)
        self.assertEqual("15",self.match.getScore("Player1"))
        self.assertEqual("15",self.match.getScore("Player2"))

    def testPlayerAd(self):
        self.scoreNpoints("Player1",3)
        self.scoreNpoints("Player2",3)
        self.scoreNpoints("Player1",1)
        self.assertEqual("AD",self.match.getScore("Player1"))
        self.assertEqual("40",self.match.getScore("Player2"))

    def testEqualsAfterAd(self):
        self.scoreNpoints("Player1",3)
        self.scoreNpoints("Player2",3)
        self.scoreNpoints("Player1",1)
        self.scoreNpoints("Player2",1)
        self.assertEqual("40",self.match.getScore("Player1"))
        self.assertEqual("40",self.match.getScore("Player2"))

    def testGameAfterEquals(self):
        self.scoreNpoints("Player1",3)
        self.scoreNpoints("Player2",3)
        self.scoreNpoints("Player1",1)
        self.scoreNpoints("Player2",1)
        self.scoreNpoints("Player1",2)
        self.assertEqual("0",self.match.getScore("Player1"))
        self.assertEqual("0",self.match.getScore("Player1"))
        self.assertEqual("1-0",self.match.getGamesScore())

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
