from hamiltonian import HamiltonianPath
import unittest


class HamiltonianTest(unittest.TestCase):
    def setUp(self):
        self.square_graph = [[1, 3], [2, 0], [3, 1], [0, 2]]
        self.square = HamiltonianPath(self.square_graph)

    def testSmallGraphs(self):
        self.assertRaises(ValueError, HamiltonianPath, [])
        self.assertRaises(ValueError, HamiltonianPath, [0])
        self.assertRaises(ValueError, HamiltonianPath, [[0], [1]])

    def testPendingVertex(self):
        pending = self.square.get_vertex()
        self.assertTrue(0 in pending and 1 in pending and
                        2 in pending and 3 in pending)

    def testGraphWalk(self):
        self.assertTrue(self.square.graph_walk([0, 1, 2, 3]))
        self.assertTrue(self.square.graph_walk([0, 3, 2, 1]))
        self.assertFalse(self.square.graph_walk([1, 2, 0, 3]))
        self.assertFalse(self.square.graph_walk([0, 1, 2]))

    def testPathGeneration(self):
        self.assertEqual(8, len(self.square.generate_paths()))
        self.assertTrue([0, 1, 2, 3] in self.square.generate_paths())

    def testPathsAndCycles(self):
        generated_paths = self.square.generate_paths()
        (paths, cycles) = self.square.paths_and_cycles(generated_paths)
        self.assertEqual(8, len(paths))
        self.assertEqual(8, len(cycles))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
