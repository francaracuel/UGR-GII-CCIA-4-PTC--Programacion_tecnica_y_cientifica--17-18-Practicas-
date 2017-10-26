# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programacion Técnica y Científica

4º - GII - CCIA - ETSIIT

Curso 2017/2018

Sesión 2 - Ejercicios

"""


# 1. Función que recibe un texto y devuelve true si está ordenado
# alfabéticamente y false si no lo está


def is_sorted(text):

    # Se cambia todo el texto a minúsculas
    text = str.lower(text)

    # Se supone que el texto está ordenado
    is_sorted = True

    # Contador para recorrer los caracteres, se comienza en el segundo carácter
    i = 1

    # Longitud del texto
    length = len(text)

    # Se recorren todos los caracteres hasta el final o hasta que ya se sepa
    # que no está ordenado
    while i < length and is_sorted:

        # Si no está ordenado se indica que no lo está
        if text[i-1] > text[i]:
            is_sorted = False

        # Se aumenta el contador del carácter
        i += 1

    return is_sorted


# 2. Función que comprueba si en el primer parámetro aparecen todas las letras
# que aparecen en el segundo


def is_in_text(text, subtext):

    # Se cambian todas las letras a minúsculas
    text = str.lower(text)
    subtext = str.lower(subtext)

    is_in_text = True

    # Lista para guardar si ya se ha comprobado una letra
    checked = dict()

    # Contador de la subcadena
    i = 0

    # Longitud de la cadena que se quiere comprobar
    length_subtext = len(subtext)

    # Se recorre toda la subcadena
    while i < length_subtext:

        # Se comprueba si ya ha sido comprobado el carácter
        if subtext[i] not in checked:

            # Se indica que el carácter no ha sido encontrado
            find = False

            # Contador para recorrer la cadena principal
            j = 0

            # Longitud de la cadena principal
            length_text = len(text)

            # Se recorre la cadena principal para buscar el carácter
            while j < length_text and not find:

                # Si coincide el carácter, se termina el ciclo y se añade al
                # diccionario
                if text[j] == subtext[i]:

                    find = True
                    checked[subtext[i]] = subtext[i]

                j += 1

            # Si no se ha encontrado, no está en el texto
            is_in_text = find

        i += 1

    return is_in_text


# 3. Función que comprueba si tiene tres parejas seguidas


def triple_double(text):

    # Se cambia todo a minúsculas
    text = str.lower(text)

    # Se cuenta con que no tiene las tres parejas dobles
    has = False

    # Contador para iterar por los caracteres
    i = 0

    length = len(text)

    # Si la longitud es menor que 6 no puede tenerlas
    if length >= 6:

        # Se recorren los carácteres hasta que se llega al fin. Se para cuando
        # queden menos de 6 caracteres por comprobar
        while i <= length-6 and not has:

            # Como se sabe seguro que no habrá desbordamiento al acceder a las
            # posiciones del texto, se comprueba directamente si existen las 3
            # parejas seguidas
            if (text[i] == text[i+1]) and (text[i+2] == text[i+3]) and (text[i+4] == text[i+5]):
                has = True

            i += 1

    return has


# 4. Función que devuelva troceada la cadena recibida en cadenas de tamaño num


def cut_text(text, num=5):

    # La lista comienza estando vacía
    l = list()

    # Contador
    i = 0

    # Longitud de la cadena
    length = len(text)

    # Se itera tantas veces como sea la longitud de la cadena y sea num
    while i < length:

        l.append(text[i: i+num])

        i += num

    return l


# 5. Comprobar si una palabra es un anagrama de otra palabra


def is_anagram(text1, text2):

    # Se convierten los dos textos a minúsculas
    text1 = str.lower(text1)
    text2 = str.lower(text2)

    # Se crean dos listas
    l1 = list(text1).sort()
    l2 = list(text2).sort()

    # Se comienza indicand que no son anagramas
    is_anagram = False

    # Se comprueba que el tamaño sea igual
    if l1 == l2:
        is_anagram = True

    return is_anagram

# Se ejecuta solo si es el fichero principal
if __name__ == "__main__":

    text = "pajarito"
    subtext = "otirajap"

    print("\nSesión 2")

    print("----------")

    print("\nCadena: %s" % text)
    print("\nSubcadena: %s" % subtext)

    print("\n----------\n")

    ########
    # Ejercicio 1
    #

    print("\nEjercicio 1:\n")

    if is_sorted(text):
        print("El texto está ordenado")

    else:
        print("El texto no está ordenado")

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 2
    #

    print("\nEjercicio 2:\n")

    if is_in_text(text, subtext):
        print("Aparecen todas las letras")

    else:
        print("No aparecen todas las letras")

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 3
    #

    print("\nEjercicio 3:\n")

    if triple_double(text):
        print("Aparecen tres parejas seguidas")

    else:
        print("No aparecen tres parejas seguidas")

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 4
    #

    print("\nEjercicio 4:\n")

    print(cut_text(text))

    print("\n----------\n")

    #
    ########

    ########
    # Ejercicio 5
    #

    print("\nEjercicio 5:\n")

    if is_anagram(text, subtext):
        print("La cadena %s es anagrama de %s" % (text, subtext))

    else:
        print("La cadena %s no es anagrama de %s" % (text, subtext))

    print("\n----------\n")

    #
    ########
