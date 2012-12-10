import unittest
from Fizzbuzz import *

class FizzbuzzTests(unittest.TestCase):

    def setUp(self):
        self.fizzbuzz = Fizzbuzz()

    def testAsk1(self):
        self.assertEqual("1",self.fizzbuzz.answerQuestion(1))

    def testAsk3(self):
        self.assertEqual("Fizz",self.fizzbuzz.answerQuestion(3))

    def testAsk5(self):
        self.assertEqual("Buzz",self.fizzbuzz.answerQuestion(5))

    def testAsk15(self):
        self.assertEqual("FizzBuzz",self.fizzbuzz.answerQuestion(15))

    def testAsk35(self):
        self.assertEqual("FizzBuzz",self.fizzbuzz.answerQuestion(35))

    def testPrintAll(self):
        for number in range(1,100):
            print self.fizzbuzz.answerQuestion(number)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()

