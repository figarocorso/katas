import unittest
from tennis import TennisGame


class TennisGameTest(unittest.TestCase):

    def test_new_game_starts_at_love_all(self):
        game = TennisGame("Player 1", "Player 2")
        self.assertEqual("love-all", game.score())

    def test_player1_scores_one_point(self):
        game = TennisGame("Player 1", "Player 2")
        game.won_point("Player 1")
        self.assertEqual("fifteen-love", game.score())

    def test_player2_scores_one_point(self):
        game = TennisGame("Player 1", "Player 2")
        game.won_point("Player 2")
        self.assertEqual("love-fifteen", game.score())


if __name__ == '__main__':
    unittest.main()
