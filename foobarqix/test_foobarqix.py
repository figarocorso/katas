import unittest

from foobarqix import FooBarQix


class TestFooBarQix(unittest.TestCase):

    def setUp(self):
        self.foobarqix = FooBarQix()

    def test_1(self):
        self.assertEqual("1", self.foobarqix.compute("1"))

    def test_no_compute(self):
        self.assertEqual("2", self.foobarqix.compute("2"))
        self.assertEqual("4", self.foobarqix.compute("4"))
        self.assertEqual("8", self.foobarqix.compute("8"))

    def test_divisible_by_3(self):
        self.assertEqual("Foo", self.foobarqix.compute("6"))

    def test_contains_a_3(self):
        self.assertEqual("Foo", self.foobarqix.compute("13"))

    def test_contains_a_3_and_divisible_by_3(self):
        self.assertEqual("FooFoo", self.foobarqix.compute("3"))

    def test_divisible_by_5(self):
        self.assertEqual("Bar", self.foobarqix.compute("20"))

    def test_contains_5_and_divisible_by_5(self):
        self.assertEqual("BarBar", self.foobarqix.compute("5"))

    def test_divisible_by_3_and_5_contains_a_5(self):
        self.assertEqual("FooBarBar", self.foobarqix.compute("45"))

    def test_divisible_by_7_and_contains_a_7(self):
        self.assertEqual("QixQix", self.foobarqix.compute("7"))

    def test_contains_5_and_7_unordered(self):
        self.assertEqual("FooBarQixBar", self.foobarqix.compute("75"))

    def test_contains_multiple_7(self):
        self.assertEqual("FooQixQixQixQix", self.foobarqix.compute("777"))

    def test_contains_3_and_5_and_7_unordered(self):
        self.assertEqual("FooQixBarFoo", self.foobarqix.compute("753"))

if __name__ == "__main__":
    unittest.main()
