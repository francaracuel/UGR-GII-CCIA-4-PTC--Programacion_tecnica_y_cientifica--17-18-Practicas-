# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programacion Técnica y Científica

4º - GII - CCIA - ETSIIT

Curso 2017/2018

Sesión 8 - Ejercicios

"""

################################################################################
# Funciones
#

########
# Ejemplo 1
#

def cubo(x):
    """
    La función cubo devuelve x*x*x
    >>> cubo(3)
    27
    >>> cubo (-1)
    -1
    """

    return x*x*x

#
########

########
# Ejemplo 2
#

def cuadrados(a, b):
    """
    Devuelve todos los cuadrados en el rango a..b
    >>> cuadrados(1 ,10)
    [1, 4, ..., 100]
    """
    res=[]
    for i in range(a,b+1):
        res.append(i*i)
    return res

#
########

########
# Ejemplo 3
#

def square(x):
    """
    Esta función eleva un número al cuadrado
    >>> square(-3)
    9
    >>> square(16)
    Traceback (most recent call last):
      ...
    ValueError: input too large
    """
    if x > 10:
        raise ValueError('input too large')
    else:
        return x*x

#
########

########
# Ejercicio 1
#

def suma(a, b):
    """
    La función devuelve la suma del rango entre a y b
    >>> suma(1, 2)
    3
    >>> suma(-10, 10)
    0
    >>> suma(5, 5)
    5
    """
    res = 0
    for i in range(a, b+1):
        res = res + i
    return res

#
########

########
# Ejercicio 2
#

def ordenar(a):
    """
    La función ordena los elementos de cualquier vector recibido
    >>> ordenar([1, 2, 4, 5, 3, 10])
    [1, 2, 3, 4, 5, 10]
    >>> ordenar(range(1, 1000))
    [1, ..., 999]
    >>> ordenar(['a', 'c', 'b', 'm', 'z', 'e'])
    ['a', 'b', 'c', 'e', 'm', 'z']
    >>> ordenar([])
    []
    """

    # Se crea una lista donde se van a guardar los elementos ordenados
    sorted_list = list()

    # Se recorren todos los elementos de la lista
    for i in a:

        pos = 0

        # Siempre que el elemento actual sea mayor que pos, se aumenta pos
        while(i > a[pos]):

            pos += 1

        # Cuando ya se sabe la posición que debe ocupar, se inserta
        sorted_list.insert(pos, i)

    return sorted_list

#
########

#
################################################################################

################################################################################
# Ejecuciones
#

if __name__ == '__main__':

    import doctest

    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)


########
# Ejercicio

    #print(cuadrados(1, 10));

#
########


#
################################################################################
