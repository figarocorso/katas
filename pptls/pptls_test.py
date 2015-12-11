import unittest
from pptls import PPTLS


class TestPPTLS(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_scissors(self):
        pptls = PPTLS()
        self.assertEqual(1, pptls.check_winner("scissors", "paper"))
        self.assertEqual(2, pptls.check_winner("lizard", "rock"))
        self.assertEqual(2, pptls.check_winner("scissors", "rock"))
        self.assertEqual(2, pptls.check_winner("scissors", "spock"))
        self.assertEqual(2, pptls.check_winner("rock", "Spock"))
        self.assertEqual(2, pptls.check_winner("spock", "lizard"))
        self.assertEqual(2, pptls.check_winner("paper", "lizard"))
        self.assertEqual(2, pptls.check_winner("rock", "paper"))
        self.assertEqual(2, pptls.check_winner("spock", "paper"))
        self.assertEqual(2, pptls.check_winner("paper", "scissors"))
        self.assertEqual(2, pptls.check_winner("lizard", "scissors"))

    def test_tie(self):
        pptls = PPTLS()
        self.assertEqual(0, pptls.check_winner("spock", "spock"))

    def test_capital_letters(self):
        pptls = PPTLS()
        self.assertEqual(2, pptls.check_winner("scissors", "Spock"))
        self.assertEqual(2, pptls.check_winner("Scissors", "Spock"))


if __name__ == "__main__":
    unittest.main()
