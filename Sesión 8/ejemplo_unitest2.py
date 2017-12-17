# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:36:58 2017

@author: silve
"""

import random
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = list(range(10))

    def test_shuffle(self):
        # Asegúrate de que la secuencia barajada no pierde ningún elemento
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))

        # una excepción si la secuencia es inmutable
        self.assertRaises(TypeError, random.shuffle, (1,2,3))
    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()
