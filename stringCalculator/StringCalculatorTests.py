import unittest
from StringCalculator import StringCalculator

class StringCalculatorTest(unittest.TestCase):

    def setUp(self):
       self.stringCalculator = StringCalculator()

    def testSumEmptyString(self):
        self.assertEqual("0",self.stringCalculator.add(""))

    def testSumOneValue(self):
        self.assertEqual("1",self.stringCalculator.add("1"))

    def testSumTwoValues(self):
        self.assertEqual("3",self.stringCalculator.add("1,2"))

    def testSum15Values(self):
        self.assertEqual(str(16*7+8),self.stringCalculator.add(self.string15()))

    def testSumTwoNewLinedString(self):
        self.assertEqual("3",self.stringCalculator.add("1\n2"))

    def testDefaultDelimiterSemiColom(self):
        self.assertEqual("3",self.stringCalculator.add("//;\n1;2"))

    def testNegativeValue(self):
        self.assertRaises(self.stringCalculator.NegativeNumbers,self.stringCalculator.add,"-1,2")

    def testANegativeValueMessage(self):
        self.assertRaisesRegexp(self.stringCalculator.NegativeNumbers,"^-1$",self.stringCalculator.add,"-1,2")

    def testNegativeValuesMessage(self):
        self.assertRaisesRegexp(self.stringCalculator.NegativeNumbers,"^-1,-2$",self.stringCalculator.add,"-1,-2,3")

    def testValuesOver1000(self):
        self.assertEqual("1003",self.stringCalculator.add("1,2,1000,1001"))

    def testMultipleCharDelimiter(self):
        self.assertEqual("3",self.stringCalculator.add("//[**]\n1**2"))

    def testMultipleCharMultipleDelimiter(self):
        self.assertEqual("6",self.stringCalculator.add("//[**][perra]\n1**2perra3"))

    def tearDown(self):
        pass

    def string15(self):
        string15 = ""

        for number in range (0,16):
            string15 += str(number)
            string15 += ","

        string15 = string15.strip(",")

        return string15

if __name__ == "__main__":
    unittest.main()
