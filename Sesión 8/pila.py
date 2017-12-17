# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programacion Técnica y Científica

4º - GII - CCIA - ETSIIT

Curso 2017/2018

Sesión 8 - Clase Pila

"""

################################################################################
# Clase Pila
#

class pila:
    """
    Clase Pila
    """

    ########
    # Constructor
    #
    def __init__(self):
        """
        Constructor de la clase Pila. Inicializa una lista
        """

        self.pila = list()

    ########
    # Utils
    #
    def add_item(self, *elements):
        """
        Añade una serie de elementos a la lista
        """

        for i in elements:
            self.pila.append(i)

    def pop_item(self):
        """
        Elimina el primer elemento de la lista
        """

        value = len(self.pila)

        if value > 0:

            value = self.pila[value-1]

            del self.pila[-1]

        return value

    def count_items(self):
        """
        Devuelve el número de elementos que tiene la lista
        """

        return len(self.pila)

#
################################################################################
