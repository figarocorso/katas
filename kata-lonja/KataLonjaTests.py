import unittest
from KataLonja import *

class KataLonjaTests(unittest.TestCase):

    def setUp(self):
        self.lonja = KataLonja()

    def testSeaFoodValue(self):
        self.assertEqual(47500,self.lonja.saleValue("Madrid"))

    def testTransportCost(self):
        self.assertEqual(5405,self.lonja.transportCost("Madrid"))

    def testRevenue(self):
        self.assertEqual(42095,self.lonja.revenueShippingTo("Madrid"))

    def testSolveProblem(self):
        self.assertEqual("Lisboa",self.lonja.bestCityToShip(["Madrid","Barcelona","Lisboa"]))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
