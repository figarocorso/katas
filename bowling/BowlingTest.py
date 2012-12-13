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
        self.assertEqual(58,self.bowling.calculateRoll("1//11XX1111-11111"))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
