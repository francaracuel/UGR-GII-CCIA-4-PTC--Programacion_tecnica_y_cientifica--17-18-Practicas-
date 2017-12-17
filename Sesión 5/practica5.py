# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programacion Técnica y Científica

4º - GII - CCIA - ETSIIT

Curso 2017/2018

Sesión 5 - Ejercicios

"""


########
# Ejercicio 1
#


def factores_primos(n):

    l = list()

    div = True

    coc = 2

    i = 0

    # Mientras que se pueda seguir diviendo, se sigue haciendo comprobaciones
    while(div):

        # Cuando ya no sea necesario seguir comprobando, se indica que pare
        if(n == 1):

            # Si el último cociente tenía algún elemento, se añade a la lista
            if(i != 0):
                    l.append((coc, i))

            div = False

        else:

            # Si es múltiplo, se disminuye el número y se aumenta su contador
            if(n % coc == 0):
                n = n/coc
                i += 1

            else:

                # Si se llega a este punto, la última vez no se pudo dividir.
                # Se comprueba si se ha dividido alguna vez y si es así se
                # añade a la lista
                if(i != 0):
                    l.append((coc, i))

                # Si el cociente es 2, el siguiente es 3.
                # Si el cociente es impar, el siguiente será impar.
                if(coc == 2):
                    coc = 3
                else:
                    coc += 2

                # Se resetea el contador de múltiplos
                i = 0

    return l

#
########
    
########
# Ejercicio 2
#


def numero(factores):

    res = 1

    for i, v in factores:
        res *= pow(i, v)

    return res

#
########

########
# Ejercicio 3
    
# Hacer la multiplicación de 2 matrices
def mul(m1, m2):
    
    # Si no coinciden filas y columnas devuelve -1
    res = -1
    
    rows1 = len(m1)
    cols1 = len(m1[0])
    rows2 = len(m2)
    cols2 = len(m2[0])
    
    # Se comprueba que coincidan las filas y las columnas de las matrices
    if(rows1 == cols2):
        
        res = [[0]*cols2]*rows1
        
        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    res[i][j] += m1[i][k]*m2[k][j]
    
    return res

#
########

########
# Ejercicio 4
#

# Construye en vector que indica el valor y posición que ocupa un valor 
# distinto de 0 y el tamaño total de elementos
def vector_disperso(v):
    
    l = list()
    
    i = 0
    
    for i, value in enumerate(v):
        
        if value != 0:
            l.append((i, value))
    
    return (l, len(v))


#
########
    
########
# Ejercicio 5
    
def get_vector_disperso(v):
    
    l = [0]*v[1]
    
    vector = v[0]
    
    for i, value in vector:
        l[i] = value
    
    return l
    
    

#
########

# Se ejecuta solo si es el fichero principal
if __name__ == "__main__":

    # gen_random_list()

    l1 = [[1, 2, 3], [4, 5, 6]]
    l2 = [[1, 2], [3, 4], [5, 6]]

    l3 = [1, 0, 0, 3, 4, 7, 0 , 0, 2]

    n = 9

    print("\nSesión 5")

    print("----------")

    print("\nLista 1: %s" % l1)
    print("\nLista 2: %s" % l2)

    print("\n----------\n")

    ########
    # Ejercicio 1
    #

    print("\nEjercicio 1:\n")

    print("Los factores primos son:", factores_primos(n))

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 2
    #

    print("\nEjercicio 2:\n")

    print("El numero es:", numero(factores_primos(n)))

    print("\n----------\n")

    #
    ########
    
    ########
    # Ejercicio 3
    #

    print("\nEjercicio 3:\n")

    print("La matriz resultante es:", mul(l1, l2))

    print("\n----------\n")

    #
    ########
    
    ########
    # Ejercicio 4
    #

    print("\nEjercicio 4:\n")

    print("El resultado de comprobar el vector disperso es:", 
          vector_disperso(l3))

    print("\n----------\n")

    #
    ########
    
    ########
    # Ejercicio 4
    #

    print("\nEjercicio 5:\n")

    print("El vector disperso es:", get_vector_disperso(vector_disperso(l3)))

    print("\n----------\n")

    #
    ########
