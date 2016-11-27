import unittest
from karate_chop import KarateChop


class TestKarateChop(unittest.TestCase):
    def setUp(self):
        pass

    def test_zero_element(self):
        self.assertFalse(KarateChop([]).chop(5))

    def test_one_elemant(self):
        self.assertFalse(KarateChop([5]).chop(1))
        self.assertTrue(KarateChop([5]).chop(5))

    def test_two_elements(self):
        self.assertTrue(KarateChop([5, 1]).chop(5))
        self.assertFalse(KarateChop([5, 1]).chop(2))

    def test_multi_even(self):
        self._assert_true_all_elements_in_set([1, 5, 6, 62, 66, 75])
        self.assertFalse(KarateChop([1, 5, 6, 62, 66, 75]).chop(65))

    def test_multi_odd(self):
        self._assert_true_all_elements_in_set([1, 5, 6, 62, 66, 75, 99])
        self.assertFalse(KarateChop([1, 5, 6, 62, 66, 75, 99]).chop(65))

    def _assert_true_all_elements_in_set(self, test_set):
        for set_item in test_set:
            self.assertTrue(KarateChop(test_set).chop(set_item))


if __name__ == '__main__':
    unittest.main()
