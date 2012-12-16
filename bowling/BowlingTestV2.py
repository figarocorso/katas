from  BowlingV2 import BowlingV2
import unittest

class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.bowling = BowlingV2()

    def testOnePinPerThrow(self):
        self.assertEqual(20,self.bowling.calculateRoll("11111111111111111111"))

    def testRollWithMiss(self):
        self.assertEqual(18,self.bowling.calculateRoll("111111-111-111111111"))

    def testRollWithSpareNotAccumulative(self):
        self.assertEqual(27,self.bowling.calculateRoll("1/1111-111-111111111"))

    def test9AndMiss(self):
       self.assertEqual(90,self.bowling.calculateRoll("9-9-9-9-9-9-9-9-9-9-"))

    def test5AndSpareAnd5(self):
       self.assertEqual(150,self.bowling.calculateRoll("5/5/5/5/5/5/5/5/5/5/5"))

    def testAllStrikes(self):
        self.assertEqual(300,self.bowling.calculateRoll("XXXXXXXXXXXX"))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
