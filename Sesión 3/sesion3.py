# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programacion Técnica y Científica

4º - GII - CCIA - ETSIIT

Curso 2017/2018

Sesión 3 - Ejercicios

"""

########
# Ejercicio 1
#

def is_panogram(text, alph = "abcdefghijklmnñopqrstuvwxyz"):

    is_pgrm = True

    # Se convierte todo el texto a minúsculas
    text = str.lower(text)

    # Se inicializa el contador
    i = 0

    # Longitud del alfabeto
    length = len(alph)

    # Mientras que haya alfabeto que revisar y sea un pangrama
    while (i<length) & is_pgrm:

        # Si la letra del alfabeto no está en el texto, is_pgrm se niega y se
        # termina el bucle
        if alph[i] not in text:
            is_pgrm = False

        i += 1

    return is_pgrm

#
########

########
# Ejercicio 2
#

def cesar(text, dst = 1):
    """
    Encripta un texto utilizando el sistema César. Si se quiere desencriptar,
    se le envía por parámetro el número negativo.
    """

    res = ""

    for char in text:

        res += chr(ord(char)+dst)

    return res

#
########

########
# Ejercicio 3
#

def suma_digitos(text):

    res = 0

    if isinstance(text, int):
        text = str(text)

    for char in text:

        res += int(char)

    return res

#
########

########
# Ejercicio 4
#

def contar_pares(l):

    res = 0

    for i in l:

        if isinstance(i, int):
            if i%2 == 0:
                res += 1

    return res

#
########

########
# Ejercicio 5
#

def dims(l):

    t = ()

    while isinstance(l, list):

        t = t + (len(l),)

        l = l[0]


    return t

#
########

# Se ejecuta solo si es el fichero principal
if __name__ == "__main__":

    textL = "Benjamín pidió una bebida de kiwi y fresa Noé sin vergüenza la más exquisita champaña del menú"
    text = "Cadena a encriptar"
    numbers = "12345"
    list1 = ["a", "b", "c", "d", 1,2,3,4,5,6,7,8,9]
    list2 = [[[1],[2]], [[3],[4]], [[3],[4]], [[3],[4]]]

    print("\nSesión 3")

    print("----------")

    print("\nCadena: %s" % text)

    print("\n----------\n")

    ########
    # Ejercicio 1
    #

    print("\nEjercicio 1:\n")

    if is_panogram(textL):
        print("El texto es un pangrama")

    else:
        print("El texto no es un pangrama")

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 2-a
    #

    print("\nEjercicio 2:\n")

    print("Texto encriptado: ", cesar(text))

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 2-b
    #

    print("\nEjercicio 2-b:\n")

    print("Texto desencriptado: ", cesar(cesar(text), -1))

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 3
    #

    print("\nEjercicio 3:\n")

    print("Suma de ", numbers, ": ", suma_digitos(numbers))

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 3-b
    #

    print("\nEjercicio 3-b:\n")

    print("Suma de ", numbers, ": ", suma_digitos(12345))

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 4
    #

    print("\nEjercicio 4:\n")

    print("El número de pares de la lista ", list1, " es: ", contar_pares(list1))

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 5
    #

    print("\nEjercicio 5:\n")

    print("Dimensión de la lista ", list2, " es: ", dims(list2))

    print("\n----------\n")

    #
    ########
