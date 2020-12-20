import unittest


class WidthExceededException(Exception):
    pass


class DownValueNeededException(Exception):
    pass


class Slope():
    def __init__(self, right, down):
        if down <= 0:
            raise DownValueNeededException

        self.right = right
        self.down = down


class Topology():
    TREE_CHAR = '#'

    def __init__(self, topology_list):
        self.width = len(topology_list[0])
        self.heigh = len(topology_list)
        self.topology = ''.join(topology_list)
        self.restart()

    def __str__(self):
        return self.topology

    def restart(self):
        self.current_x = 0
        self.current_y = 0

    @property
    def current_position(self):
        return self.current_x + self.current_y * self.width


    def count_trees_during_slope_down(self, slope):
        trees = 0
        while not self.is_finished:
            trees += 1 if self.is_tree else 0
            self.slope_down(slope)
        return trees

    def slope_down(self, slope):
        self.current_x += slope.right
        self.current_y += slope.down
        if self.current_x >= self.width and self.current_y < self.heigh:
            raise WidthExceededException

    @property
    def is_finished(self):
        return self.current_position >= len(self.topology)

    @property
    def is_tree(self):
        return self.topology[self.current_position] == self.TREE_CHAR


class TopologySlopeTest(unittest.TestCase):
    def setUp(self):
        topology_list = [
            '..##.........##.........##.........##.........##.........##.......',
            '#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..',
            '.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.',
            '..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#',
            '.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.',
            '..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....',
            '.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#',
            '.#........#.#........#.#........#.#........#.#........#.#........#',
            '#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...',
            '#...##....##...##....##...##....##...##....##...##....##...##....#',
            '.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#',
        ]
        self.topology = Topology(topology_list)

    def test_topology_init(self):
        self.assertEqual('abc', str(Topology(['a', 'b', 'c'])))
        self.assertEqual(726, len(str(self.topology)))
        self.assertEqual(66, self.topology.width)

    def test_slope_down_only_down(self):
        slope = Slope(0, 1)
        self.assertEqual(0, self.topology.current_position)
        self.topology.slope_down(slope)
        self.assertEqual(self.topology.width, self.topology.current_position)
        self.topology.slope_down(slope)
        self.assertEqual(self.topology.width * 2, self.topology.current_position)

    def test_slope_down(self):
        slope = Slope(3, 1)
        self.assertEqual(0, self.topology.current_position)
        self.topology.slope_down(slope)
        self.assertEqual(slope.right + self.topology.width, self.topology.current_position)
        self.topology.slope_down(slope)
        self.assertEqual(slope.right * 2 + self.topology.width * 2, self.topology.current_position)

    def test_slope_down_over_right(self):
        slope = Slope(self.topology.width, 1)
        self.assertRaises(WidthExceededException, self.topology.slope_down, slope)

    def test_slope_down_only_right(self):
        self.assertRaises(DownValueNeededException, Slope, 1, 0)

    def test_is_finished(self):
        self.assertFalse(self.topology.is_finished)
        self.topology.slope_down(Slope(3, 1))
        self.assertFalse(self.topology.is_finished)
        self.topology.slope_down(Slope(3, self.topology.heigh + 3))
        self.assertTrue(self.topology.is_finished)

    def test_type_of_square_tree(self):
        slope = Slope(0, 1)
        self.assertFalse(self.topology.is_tree)
        self.topology.slope_down(slope)
        self.assertTrue(self.topology.is_tree)
        self.topology.slope_down(slope)
        self.assertFalse(self.topology.is_tree)
        self.topology.slope_down(slope)
        self.assertFalse(self.topology.is_tree)

    def test_restart(self):
        self.assertEqual(0, self.topology.current_position)
        self.topology.slope_down(Slope(0, 1))
        self.assertEqual(self.topology.width, self.topology.current_position)
        self.topology.restart()
        self.assertEqual(0, self.topology.current_position)

    def test_count_trees_3_1(self):
        self.assertEqual(7, self.topology.count_trees_during_slope_down(Slope(3, 1)))
        self.topology.restart()
        self.assertEqual(3, self.topology.count_trees_during_slope_down(Slope(0, 1)))

    def test_count_trees_not_finished(self):
        slope = Slope(30, 1)
        self.assertRaises(WidthExceededException, self.topology.count_trees_during_slope_down, slope)


if __name__ == '__main__':
    unittest.main()
