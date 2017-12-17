# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:34:01 2017

@author: silve
"""

import unittest

def fun(x):
    return x + 1
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

if __name__ == '__main__':
    unittest.main(exit=False)
    # se usa exit pare definir que el intérprete pare
