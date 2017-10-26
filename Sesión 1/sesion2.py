# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programacion Técnica y Científica - 4º - GII - CCIA - ETSIIT

Curso 2017/2018

"""


# 1. Función que reciba una cadena y una letra y devuelva el número
# de veces que aparece la letra en la cadena.
def count_char(st, char):

    res = 0

    # Se recorre la cadena y en caso de ser igual se aumenta eontador
    for c in st:
        if c == char:
            res = res + 1

    return res


# 2. Eliminar la letra que se reciba por parámetro y devolver la cadena sin 
# ella
def remove_char(st, char):

    res = ""

    for c in st:
        if c != char:
            res += c

    return res


# 3. Intercambia las letras mayúsculas y minúsculas
def swap_upper_lower(st):

    res = ""

    # Se guardan los números correspondientes a las letras del extremo del 
    # abecedario
    n_A = ord('A')
    n_Z = ord('Z')
    n_a = ord('a')
    n_z = ord('z')

    # Se guarda el valor que se debe sumar o restar a la letra
    diff = abs(ord('A') - ord('a'))

    for c in st:

        # Se guarda el número correspondiente a la letra actual de la cadena
        n_c = ord(c)

        # Si la letra pertenece a las mayúsculas
        if n_c >= n_A & n_c <= n_Z:
            res += chr(n_c - diff)
        elif n_c >= n_a & n_c <= n_z:
            res += chr(n_c + diff)
        else:
            res += c

    return res


# 4. Busca la posición donde se encuentra la subcadena. Devuelve -1 si no está
def find(st, sub_st):

    res = 0

    i_st = 0
    i_sub_st = 0

    len_st = len(st)
    len_sub_st = len(sub_st)

    find = False

    while (not find) & (len_st > i_st) & (len_sub_st > i_sub_st):

        if st[i_st] == sub_st[i_sub_st]:
            find = True

        i_st = i_st + 1

    if find:

        res = i_st

        while (find) & (len_st > i_st) & (len_sub_st > i_sub_st):

            if st[i_st] != sub_st[i_sub_st]:
                find = False

            i_st = i_st + 1
            i_sub_st = i_sub_st + 1

    return res


# 5. Comprobar que dadas dos cadenas, una es la inversa de la otra
def inv(cad1, cad2):

    res = True

    # Se comprueba si tienen la misma longitud
    if len(cad1) != len(cad2):
        res = False

    if res:

        # Se recorren las dos cadenas, una en sentido normal y otra en sentido
        # inverso y se comprueban si son iguales sus caracteres
        for c1, c2 in zip(cad1, cad2[::-1]):

            if c1 != c2:
                res = False

    return res - 1

# %%


# Se ejecuta solo si es el fichero principal
if __name__ == "__main__":

    # Elementos a buscar
    st = "hola"
    st2 = "aloh"
    char = "o"

    # Se muestra la cadena y la letra
    print("La cadena es: %s." % (st))
    print("La letra es: %s." % (char))

    # Llamada a la función que cuenta la letra
    nc_1 = count_char(st, char)

    # Se muestra el resultado
    print("El número de veces que aparece la letra %s es %d." % (char, nc_1))

    # Llamada a la función que elimina una letra de la cadena
    st_2 = remove_char(st, char)

    # Se muestra el resultado
    print("La cadena sin la letra %s es %s." % (char, st_2))

    # Llamada a la función que intercambia mayúsculas y minúsculas
    st_3 = swap_upper_lower(st)

    # Se muestra el resultado
    print("La cadena intercambiada es %s." % st_3)

    # Llamada a la función que devuelve la posición de la subcadena
    pos_st4 = find(st, char)

    # Se muestra el resultado
    print("La posición de la subcadena es: %d" % pos_st4)

    # Llamada a la función que comprueba si dos cadenas son inversas
    inv_5 = inv(st, st2)

    # Se muestra el resultado
    if inv_5:
        print("Las cadenas %s y %s son inversas." % (st, st2))
    else:
        print("Las cadenas %s y %s no son inversas." % (st, st2))
