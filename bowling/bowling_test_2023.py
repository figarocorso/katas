from  bowling_2023 import Game
import unittest

class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()


    def test_initial_score(self):
        self.assertEquals(self.game.score(), 0)

    def test_one_open_frame(self):
        self.game.roll(6)
        self.game.roll(2)
        self.assertEquals(self.game.score(), 8)

    def test_two_open_frame(self):
        self.game.roll(6)
        self.game.roll(2)
        self.game.roll(6)
        self.game.roll(2)
        self.assertEquals(self.game.score(), 16)

    def test_one_spare(self):
        self.game.roll(6)
        self.game.roll(4)
        self.game.roll(6)
        self.game.roll(0)
        self.assertEquals(self.game.score(), 22)

    def test_two_spares(self):
        self.game.roll(6)
        self.game.roll(4)
        self.game.roll(6)
        self.game.roll(4)
        self.game.roll(6)
        self.game.roll(0)
        self.assertEquals(self.game.score(), 38)

    def test_two_spares(self):
        self.game.roll(10)
        self.game.roll(6)
        self.game.roll(4)
        self.game.roll(6)
        self.game.roll(0)
        self.assertEquals(self.game.score(), 42)

    def test_full_example(self):
        self.game.roll(6)
        self.game.roll(2)
        self.game.roll(7)
        self.game.roll(2)
        self.game.roll(3)
        self.game.roll(4)
        self.game.roll(8)
        self.game.roll(2)
        self.game.roll(9)
        self.game.roll(0)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(6)
        self.game.roll(3)
        self.game.roll(8)
        self.game.roll(2)
        self.game.roll(7)
        self.assertEquals(self.game.score(), 153)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
