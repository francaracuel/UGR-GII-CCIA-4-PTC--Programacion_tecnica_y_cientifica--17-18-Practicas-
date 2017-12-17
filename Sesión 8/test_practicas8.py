# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programacion Técnica y Científica

4º - GII - CCIA - ETSIIT

Curso 2017/2018

Sesión 8 - Ejercicios

Clase de Test

"""

import unittest
import practicas8

class testP8(unittest.TestCase):

    def setUp(self):
        """
        Se ejecuta antes de cada test
        """

        self.res1 = practicas8.suma(1, 3)
        self.res2 = practicas8.suma(1, 1)
        self.res3 = practicas8.suma(-10, 10)


    def tearDown(self):
        """
        Se ejecuta después de cada test
        """

        pass

    def test1(self):
        """

        """

        self.assertEqual(self.res1, 6)

    def test2(self):
        """

        """

        self.assertEqual(self.res2, 1)

    def test3(self):
        """

        """

        self.assertEqual(self.res3, 0)


if __name__ == '__main__':

    unittest.main()
