import unittest
from pila import *

class TestMipila(unittest.TestCase):
    def setUp(self):
        self.mipila = pila()
        self.mipila.add_item(10);
        self.mipila.add_item(20);
        self.mipila.add_item(22, 33);

    def test_flow(self):
        self.assertEqual(self.mipila.pop_item(), 33)
        self.assertEqual(self.mipila.pop_item(), 22)
        self.assertEqual(self.mipila.count_items(), 2)
        while self.mipila.pop_item(): pass

        self.assertEqual(self.mipila.count_items(), 0)

if __name__ == "__main__" :
    unittest.main()
