# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programación Técnica y Científica

4º - GII - CCIA - ETSIIT - UGR

Curso 2017/2018

Práctica 1 - Gestión de datos metereológicos proporcionados por la AEMET

Clase File

"""

# Se importan las clases necesarias para trabajar con los datos
import pickle

################################################################################
# Clase File
#
class File_Class:
    """

    """

    ########
    # Constructor
    #
    def __init__(self):
        """

        """

    #
    ########

    ########
    # Utils
    #

    def save(self, obj, filename):
        """
        Guarda en el fichero el objeto recibido
        """

        f = open(filename, 'wb')

        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        """
        Carga del fichero el objeto recibido
        """

        f = open(filename, 'rb')

        return pickle.load(f)

    #
    ########

#
################################################################################
