import unittest
from primeFactors import PrimeFactors

class PrimeFactorsTest(unittest.TestCase):
    def setUp(self):
       self.factors = PrimeFactors()

    def testDivides(self):
        self.assertTrue(self.factors.divides(13,13))
        self.assertTrue(self.factors.divides(13,1))
        self.assertTrue(self.factors.divides(12,6))

    def testIsPrime(self):
        self.assertTrue(self.factors.is_prime(37))
        self.assertFalse(self.factors.is_prime(78))

    def testObtainFirstPrimeFactor(self):
        self.assertEqual((2), self.factors.get_first_factor(68))
        self.assertEqual((2), self.factors.get_first_factor(34))
        self.assertEqual((17), self.factors.get_first_factor(17))

    def testGetAllPrimeFactors(self):
        self.assertEqual([1,2,2,17], self.factors.get_prime_factors(68))
        self.assertEqual([1,17], self.factors.get_prime_factors(17))
        self.assertEqual([1], self.factors.get_prime_factors(1))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
