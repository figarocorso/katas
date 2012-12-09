import unittest
from RomanNumerals import *

class RomanNumeralsTest(unittest.TestCase):

    def setUp(self):
        self.romanNumerals = RomanNumerals()

    def testZeroConversion(self):
        self.assertEqual("Oops! We have not implemented it yet",self.romanNumerals.convert(0))

    def testUnitsConversion(self):
        self.assertEqual("I",self.romanNumerals.convert(1))
        self.assertEqual("II",self.romanNumerals.convert(2))
        self.assertEqual("III",self.romanNumerals.convert(3))
        self.assertEqual("IV",self.romanNumerals.convert(4))
        self.assertEqual("V",self.romanNumerals.convert(5))
        self.assertEqual("VI",self.romanNumerals.convert(6))
        self.assertEqual("VII",self.romanNumerals.convert(7))
        self.assertEqual("VIII",self.romanNumerals.convert(8))
        self.assertEqual("IX",self.romanNumerals.convert(9))

    def testTensConversion(self):
        self.assertEqual("X",self.romanNumerals.convert(10))
        self.assertEqual("XX",self.romanNumerals.convert(20))
        self.assertEqual("XXX",self.romanNumerals.convert(30))
        self.assertEqual("XL",self.romanNumerals.convert(40))
        self.assertEqual("L",self.romanNumerals.convert(50))
        self.assertEqual("LX",self.romanNumerals.convert(60))
        self.assertEqual("LXX",self.romanNumerals.convert(70))
        self.assertEqual("LXXX",self.romanNumerals.convert(80))
        self.assertEqual("XC",self.romanNumerals.convert(90))

    def testHundredsConversion(self):
        self.assertEqual("C",self.romanNumerals.convert(100))
        self.assertEqual("CC",self.romanNumerals.convert(200))
        self.assertEqual("CCC",self.romanNumerals.convert(300))
        self.assertEqual("CD",self.romanNumerals.convert(400))
        self.assertEqual("D",self.romanNumerals.convert(500))
        self.assertEqual("DC",self.romanNumerals.convert(600))
        self.assertEqual("DCC",self.romanNumerals.convert(700))
        self.assertEqual("DCCC",self.romanNumerals.convert(800))
        self.assertEqual("CM",self.romanNumerals.convert(900))

    def testHundredsConversion(self):
        self.assertEqual("M",self.romanNumerals.convert(1000))
        self.assertEqual("MM",self.romanNumerals.convert(2000))
        self.assertEqual("MMM",self.romanNumerals.convert(3000))

    def testNumber(self):
        self.assertEqual("MCMXC",self.romanNumerals.convert(1990))

    def testNumber1999(self):
        self.assertEqual("MCMXCIX",self.romanNumerals.convert(1999))

    def testDigit8(self):
        self.assertEqual(8,self.romanNumerals.convert("VIII"))

    def testDigit1999(self):
        self.assertEqual(1999,self.romanNumerals.convert("MCMXCIX"))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
