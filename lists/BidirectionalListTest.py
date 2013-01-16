import unittest
from BidirectionalList import *

class DirectListTest(unittest.TestCase):

    def setUp(self):
        self.list1 = BidirectionalList()

    def testAddingAElement(self):
        self.nodePerra = BidirectionalNode('perrakey','perra')
        self.assertEqual("perra", self.list1.add(self.nodePerra))

    def testProperAdding(self):
        self.assertEqual(False, self.list1.find('perrakey'))
        self.nodePerra = BidirectionalNode('perrakey','perra')
        self.assertEqual(False, self.list1.find('perrakey'))

    def testFindingAElement(self):
        self.nodePerra = BidirectionalNode('perrakey','perra')
        self.list1.add(self.nodePerra)
        self.assertEqual("perra", self.list1.find('perrakey').value)

    def testFindingAElementFromMultipleNodeList(self):
        self.nodePerra = BidirectionalNode('perrakey','perra')
        self.list1.add(self.nodePerra)
        self.node_vaca = BidirectionalNode('vacakey','vaca')
        self.list1.add(self.node_vaca)
        self.assertEqual("perra", self.list1.find('perrakey').value)

    def testFindingWrongKey(self):
        self.nodePerra = BidirectionalNode('perrakey','perra')
        self.list1.add(self.nodePerra)
        self.node_vaca = BidirectionalNode('vacakey','vaca')
        self.list1.add(self.node_vaca)
        self.assertEqual(False, self.list1.find('burrakey'))

    def testDeleteItem(self):
        self.nodePerra = BidirectionalNode('perrakey','perra')
        self.list1.add(self.nodePerra)
        self.node_vaca = BidirectionalNode('vacakey','vaca')
        self.list1.add(self.node_vaca)
        self.assertEqual('perra', self.list1.find('perrakey').value)
        self.assertEqual(True,self.list1.delete('perrakey'))
        self.assertEqual(False, self.list1.find('perrakey'))
        self.assertEqual(False,self.list1.delete('perrakey'))

    def testDeleteLastItem(self):
        self.nodePerra = BidirectionalNode('perrakey','perra')
        self.list1.add(self.nodePerra)
        self.assertEqual('perra', self.list1.find('perrakey').value)
        self.assertEqual(True,self.list1.delete('perrakey'))
        self.assertEqual(False, self.list1.find('perrakey'))
        self.assertEqual(False,self.list1.delete('perrakey'))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
