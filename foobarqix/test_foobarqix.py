import unittest

from foobarqix import FooBarQix


class TestFooBarQix(unittest.TestCase):

    def setUp(self):
        self.foobarqix = FooBarQix()

    def test_1(self):
        self.assertEqual("1", self.foobarqix.compute("1"))


    def test_2(self):
        self.assertEqual("2", self.foobarqix.compute("2"))

    def test_6(self):
        self.assertEqual("Foo", self.foobarqix.compute("6"))

    def test_3(self):
        self.assertEqual("FooFoo", self.foobarqix.compute("3"))

    def test_20(self):
        self.assertEqual("Bar", self.foobarqix.compute("20"))

    def test_5(self):
        self.assertEqual("BarBar", self.foobarqix.compute("5"))

    def test_45(self):
        self.assertEqual("FooBarBar", self.foobarqix.compute("45"))

    def test_7(self):
        self.assertEqual("QixQix", self.foobarqix.compute("7"))

    def test_75(self):
        self.assertEqual("FooBarQixBar", self.foobarqix.compute("75"))

    def test_777(self):
        self.assertEqual("FooQixQixQixQix", self.foobarqix.compute("777"))

    def test_753(self):
        self.assertEqual("FooQixBarFoo", self.foobarqix.compute("753"))

if __name__ == "__main__":
    unittest.main()
