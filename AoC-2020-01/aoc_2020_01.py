import unittest


class SumNumbersList():
    def __init__(self, goal, matching_list):
        self.elements_mask = [0 for _ in range(goal)]
        for number in matching_list:
            self.elements_mask[number] += 1

    def exists(self, element):
        return element < len(self.elements_mask) and bool(self.elements_mask[element])

    def appearances(self, element):
        return self.elements_mask[element]


class SumNumbers():
    def __init__(self, goal=2020):
        self.goal = goal

    def matching(self, matching_list):
        self.sn_list = SumNumbersList(self.goal, matching_list)
        for number in matching_list:
            target = self.goal - number
            if target == number:
                return number * number if self.sn_list.appearances(number) > 1 else 0

            if self.sn_list.exists(target):
                return number * target

        return 0


class SumNumbersTest(unittest.TestCase):
    def setUp(self):
        self.sn = SumNumbers()

    def test_initial(self):
        self.assertEqual(0, self.sn.matching([]))

    def test_two_elements(self):
        self.assertEqual(1010 * 1010, self.sn.matching([1010, 1010]))

    def test_two_wrong_elements(self):
        self.assertEqual(0, self.sn.matching([1010, 1009]))

    def test_three_elements(self):
        self.assertEqual(1010 * 1010, self.sn.matching([1010, 1010, 999]))

    def test_problem_statement(self):
        self.assertEqual(514579, self.sn.matching([1721, 979, 366, 299, 675, 1456]))


if __name__ == '__main__':
    unittest.main()
