import unittest
from DirectList import *

class DirectListTest(unittest.TestCase):

    def setUp(self):
        self.list1 = DirectList()

    def testAddingAElement(self):
        self.nodePerra = DirectNode('perrakey','perra')
        self.assertEqual("perra", self.list1.add(self.nodePerra))

    def testProperAdding(self):
        self.assertEqual(None, self.list1.find('perrakey'))
        self.nodePerra = DirectNode('perrakey','perra')
        self.assertEqual(None, self.list1.find('perrakey'))

    def testFindingAElement(self):
        self.nodePerra = DirectNode('perrakey','perra')
        self.list1.add(self.nodePerra)
        self.assertEqual("perra", self.list1.find('perrakey'))

    def testFindingAElementFromMultipleNodeList(self):
        self.nodePerra = DirectNode('perrakey','perra')
        self.list1.add(self.nodePerra)
        self.node_vaca = DirectNode('vacakey','vaca')
        self.list1.add(self.node_vaca)
        self.assertEqual("perra", self.list1.find('perrakey'))

    def testFindingWrongKey(self):
        self.nodePerra = DirectNode('perrakey','perra')
        self.list1.add(self.nodePerra)
        self.node_vaca = DirectNode('vacakey','vaca')
        self.list1.add(self.node_vaca)
        self.assertEqual(None, self.list1.find('burrakey'))

    def testDeleteItem(self):
        self.nodePerra = DirectNode('perrakey','perra')
        self.list1.add(self.nodePerra)
        self.node_vaca = DirectNode('vacakey','vaca')
        self.list1.add(self.node_vaca)
        self.assertEqual('perra', self.list1.find('perrakey'))
        self.assertEqual(True,self.list1.delete('perrakey'))
        self.assertEqual(None, self.list1.find('perrakey'))
        self.assertEqual(False,self.list1.delete('perrakey'))

    def testDeleteLastItem(self):
        self.nodePerra = DirectNode('perrakey','perra')
        self.list1.add(self.nodePerra)
        self.assertEqual('perra', self.list1.find('perrakey'))
        self.assertEqual(True,self.list1.delete('perrakey'))
        self.assertEqual(None, self.list1.find('perrakey'))
        self.assertEqual(False,self.list1.delete('perrakey'))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
