# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programacion Técnica y Científica

4º - GII - CCIA - ETSIIT

Curso 2017/2018

Sesión 4 - Ejercicios

"""

import numpy as np
import random

########
# Utils
#

def gen_random_list(n = 100, bt = 1500):

    return sorted([random.randint(0, bt) for i in range(n)])

#
########

########
# Ejercicio 1
#

def get_sorted(l1, l2):

    #l = l1+l2

    #l.sort()

    # Se crea una lista con ambas
    l_aux = l1 + l2

    l_aux_length = len(l_aux)

    # En la lista final se guarda solo el primero
    l = [l_aux[0]]

    l_length = 1

    # Se recorre la lista auxiliar y se irán colocando sus elementos en el
    # orden correspondiente
    for i in range(1, l_aux_length):

        pos = 0

        # Falta corregir que cuando la primera condición no se cumpla, que no
        # intenta hacer la segunda
        while (pos < l_length) and (l_aux[i] > l[pos]):

            pos += 1

        #print("Valor:", l_aux[i], ", Posición:", pos)

        # Se inserta el valor en su posición correspondiente
        l.insert(pos, l_aux[i])

        l_length += 1

    return l

#
########

########
# Ejercicio 2
#

def get_transpose(l):

    l = np.asarray(l)

    rows = len(l[0])

    transpose = [l[:, i].tolist() for i in range(rows)]

    return transpose

#
########

########
# Ejercicio 3
#

def get_difference(l1, l2):

    i = 0

    l1_length = len(l1)
    l2_length = len(l2)

    # Si alguna de las dos está vacía devuelve l1
    if (l1_length != 0) & (l2_length != 0):

        # Se recorre mientras que el contador de la letra no supere l2
        while i < l1_length:

            if l1[i] in l2:

                # Si se elimina un valor, la lista tiene longitud -1
                del l1[i]
                l1_length -= 1

            else:

                i += 1

    return l1

#
########

########
# Ejercicio 4
#

def count_char(text):

    text = str.lower(text)

    init = ord('a')

    length_alph = ord('z') - init

    # Se crea una lista con todas las letras inicializadas a 0
    l = [[chr(init + i), 0] for i in range(length_alph)]

    # Se aumenta 1 al contador de cada letra
    for i in text:

        l[ord(i) - init][1] += 1

    # Se devuelve una lista solo con las que sean diferentes de 0
    return list(filter(lambda x: x[1] != 0, l))

#
########

# Se ejecuta solo si es el fichero principal
if __name__ == "__main__":

    # gen_random_list()

    l1 = [1,3,5,7,9]
    l2 = [2,4,6,8,7]

    m1 = [[1,2,3], [4,5,6]]

    text1 = "patata"

    print("\nSesión 4")

    print("----------")

    print("\nLista 1: %s" % l1)
    print("\nLista 2: %s" % l2)

    print("\n----------\n")

    ########
    # Ejercicio 1
    #

    print("\nEjercicio 1:\n")

    print("Las listas mezcladas y ordenadas son:", get_sorted(l1, l2))

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 2
    #

    print("\nEjercicio 2:\n")

    print("La traspuesta de la matriz:", m1, "es:", get_transpose(m1))

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 3
    #

    print("\nEjercicio 3:\n")

    print("La diferencia de listas es:", get_difference(l1, l2))

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 4
    #

    print("\nEjercicio 4:\n")

    print("La palabara", text1, "devuelve:", count_char(text1))

    print("\n----------\n")

    #
    ########
