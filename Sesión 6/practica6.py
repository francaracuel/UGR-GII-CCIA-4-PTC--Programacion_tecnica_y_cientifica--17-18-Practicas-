# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programacion Técnica y Científica

4º - GII - CCIA - ETSIIT

Curso 2017/2018

Sesión 6 - Ejercicios

"""

import time
import random

random.seed(time.time())

########
# Ejercicio 1
#

def generar_cadena_ADN(n):
    """
    Genera una cadena aleatoria de n elementos con los caracteres ACTG.
    """

    base = ['A', 'C', 'T', 'G']

    return [base[random.randint(0, 3)] for i in range(n)]

#
########

########
# Ejercicio 2
#

def contar_letras(text):
    """
    Recibe una secuencia de caracteres y devuelve un diccionario con el
    carácter y el número de veces que aparece
    """

    d = dict()

    for c in text:

        try:
            d[c] += 1
        except KeyError:
            d[c] = 1

    return d

def contar_letras_b(text):
    """
    Recibe una secuencia de caracteres y devuelve una lista con el
    carácter y el número de veces que aparece
    """

    base = ['A', 'C', 'T', 'G']

    l = [0]*len(base)

    for c in text:

        l[base.index(c)] += 1

    return [i for i in zip(base, l)]

#
########

########
# Ejercicio 3
#

def generar_numeros(n, r = 1000):
    """
    Genera una lista de números aleatorios
    """

    return [random.randint(0, r) for i in range(n)]

#
########

########
# Ejercicio 4
#

def contar_numeros(numbers):
    """
    Recibe una lista de números y devuelve un diccionario con el
    número y el número de veces que aparece
    """

    d = dict()

    for c in numbers:

        try:
            d[c] += 1
        except KeyError:
            d[c] = 1

    return d

def contar_numeros_b(numbers, r = 1000):
    """
    Recibe una lista de números y devuelve una lista con el
    carácter y el número de veces que aparece
    """

    l = [0]*(r+1)

    for c in numbers:
        l[c] += 1

    return [(i, value) for i, value in enumerate(l)]

#
########

########
# Ejercicio 5
#

def diccionario_inverso(d):
    """
    Se le pasa un diccionario y devuelve un diccionario inverso.
    """

    d_inv = dict()

    for key, value in d.items():

        try:
            d_inv[value].append(key)
        except KeyError:
            d_inv[value] = [key]

    return d_inv

#
########

########
# Ejercicio 6
#

def diccionario_inverso_inverso(d_inv):
    """
    Invierte el diccionario invertido en la función anterior
    """

    d = dict()

    for key, value in d_inv.items():
        for i in value:
            d[i] = key

    return d

#
########

# Se ejecuta solo si es el fichero principal
if __name__ == "__main__":

    n = 1000000

    print("\nSesión 6")

    print("----------")

    print("\n----------\n")

    ########
    # Ejercicio 1
    #

    print("\nEjercicio 1:\n")

    t1 = time.time()

    cadena_ADN =  generar_cadena_ADN(n)

    t2 = time.time()-t1

    #print("La cadena es:", cadena_ADN)

    print("\nTiempo en ejecutar: ", t2)

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 2
    #

    print("\nEjercicio 2:\n")

    t1 = time.time()

    d = contar_letras(cadena_ADN)

    t2 = time.time()-t1

    print("Ejercicio 2 (diccionario):", d)

    print("\nTiempo en ejecutar: ", t2)

    ########

    t1 = time.time()

    l = contar_letras_b(cadena_ADN)

    t2 = time.time()-t1

    print("\n\nEjercicio 2 (lista):", l)

    print("\nTiempo en ejecutar: ", t2)

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 3
    #

    print("\nEjercicio 3:\n")

    t1 = time.time()

    numeros =  generar_numeros(n)

    t2 = time.time()-t1

    #print("La lista de numeros es:", numeros)

    print("\nTiempo en ejecutar: ", t2)

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 4
    #

    print("\nEjercicio 4:\n")

    t1 = time.time()

    d = contar_numeros(numeros)

    t2 = time.time()-t1

    print("Ejercicio 4 (diccionario):", d)

    print("\nTiempo en ejecutar: ", t2)

    ########

    t1 = time.time()

    l = contar_numeros_b(numeros)

    t2 = time.time()-t1

    print("\n\nEjercicio 4 (lista):", l)

    print("\nTiempo en ejecutar: ", t2)

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 5
    #

    print("\nEjercicio 5:\n")

    t1 = time.time()

    d = contar_letras(generar_cadena_ADN(5))

    d_inv =  diccionario_inverso(d)

    t2 = time.time()-t1

    print("El diccionario es:", d)

    print("El diccionario inverso es:", d_inv)

    print("\nTiempo en ejecutar: ", t2)

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 6
    #

    print("\nEjercicio 6:\n")

    t1 = time.time()

    d =  diccionario_inverso_inverso(d_inv)

    t2 = time.time()-t1

    print("El diccionario recuperado es:", d)

    print("\nTiempo en ejecutar: ", t2)

    print("\n----------\n")

    #
    ########
