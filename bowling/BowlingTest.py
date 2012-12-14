from  Bowling import Bowling
import unittest

class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.bowling = Bowling()

    def testOnePinPerThrow(self):
        self.assertEqual(20,self.bowling.calculateRoll("11111111111111111111"))

    def testRollWithMiss(self):
        self.assertEqual(18,self.bowling.calculateRoll("111111-111-111111111"))

#    def testRollWithSpareNotAccumulative(self):
#        self.assertEqual(26,self.bowling.calculateRoll("1/1111-111-111111111"))

#    def testRollWithSpareNotAccumulativeBadPreviousThrow(self):
#        self.assertEqual(34,self.bowling.calculateRoll("1//11-111-111111111"))

    def testRollWithSpare(self):
        self.assertEqual(46,self.bowling.calculateRoll("1//11-111-111111111"))

    def testRollWithSpareAndStrike(self):
        self.assertEqual(58,self.bowling.calculateRoll("1//11X11-111111111"))

    def testRollWithSpareAndTwoStrike(self):
        self.assertEqual(79,self.bowling.calculateRoll("1//11XX1111-11111"))

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
