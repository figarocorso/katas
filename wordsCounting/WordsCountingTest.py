import unittest
from WordsCounting import *

class WordsCountingTest(unittest.TestCase):

    def setUp(self):
        self.counter = WordsCounting()

    def testReadFile(self):
        self.assertEqual("foo:1\n",self.counter.count_file("one_word_file.txt"))

    def testCountAFoo(self):
        self.assertEqual("foo:1\n", self.counter.count("foo\n"))

    def testCountTwoFoos(self):
        self.assertEqual("foo:2\n", self.counter.count("foo foo\n"))

    def testCountTwoFoosAndABar(self):
        self.assertEqual("foo:2\nbar:1\n", self.counter.count("foo bar foo\n"))

    def testReadNonExistingFile(self):
        self.assertRaises(self.counter.FileNotFound, self.counter.count_file,"soy_una_vaca.txt")

    def testReadFromSampleRandomFile(self):
        print self.counter.count_file("sample_file.txt")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
