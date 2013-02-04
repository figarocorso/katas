import unittest
from minesweeper import *

class MinesweeperTest(unittest.TestCase):

    def setUp(self):
        self.minesweeper = Minesweeper(4,4)

    def test_grid_size(self):
        self.assertEqual(4,self.minesweeper.columns)
        self.assertEqual(4,self.minesweeper.rows)

    def test_set_mine(self):
        self.assertEqual('.',self.minesweeper.get_item_at(1,1))
        self.assertEqual('.',self.minesweeper.get_item_at(3,3))
        self.minesweeper.plant_mine(1,1).plant_mine(3,3)
        self.assertEqual('*',self.minesweeper.get_item_at(1,1))
        self.assertEqual('*',self.minesweeper.get_item_at(3,3))

    def test_fill_adjacent_mine_number(self):
        self.minesweeper.fill_adjacent_mine_number()

    def

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
