# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programacion Técnica y Científica

4º - GII - CCIA - ETSIIT

Curso 2017/2018

Sesión 7 - Ejercicios

"""

from math import *
from tkinter import *
import random

################################################################################
# Funciones
#

########
# Ejercicio 1-2
#

# Se unifica el ejercicio 1 y 2, añadiendo a la misma ventana el evento de
# pulsar "Enter" y un botón

def pressedButton1(parent = None):
    """
    Parent solo se mantiene por compatibilidad.
    Asigna el cuadrado de la etiqueta entryBox1_12
    """

    # Para acceder a la etiqueta debe ser global
    global entryBox1_12
    global text1

    # Guarda como entero el valor de entryBox1_12
    value1 = int(entryBox1_12.get())

    # Asigna a la etiqueta el cuadrado del número
    text1.set(value1*value1)


def main12():
    """
    Muestra una ventana donde permite escribir un número y mostrar su cuadrado
    al pulsar "Enter" o pulsar sobre el botón
    """

    global entryBox1_12
    global text1

    root1 = Tk()
    root1.geometry("200x100")

    # Se crea la primera parte del mensaje
    label1_1 = Label(root1, text="El cuadrado de ")
    label1_1.grid(row=0, column=0)

    # Se crea la caja de texto donde se escribe el número
    entryBox1_12 = Entry(root1, text="", width="10")
    entryBox1_12.grid(row=0, column=1)

    # Se le asigna el función que se va a ejecutar al pular el botón "Enter"
    entryBox1_12.bind("<Return>", pressedButton1)

    # Siguiente parte del mensaje
    label1_2 = Label(root1, text=" es:")
    label1_2.grid(row=0, column=2)

    # Para mostrar el resultado es necesario utilizar StringVar
    text1 = StringVar()
    label1_3 = Label(root1, textvariable=text1)
    label1_3.grid(row=1, columnspan=3)

    # Se crea un botón donde se le indica la función que se ejecuta al pulsar
    # sobre él
    button1 = Button(root1, text="Enviar", command=pressedButton1)
    button1.grid(row=2, columnspan=3)

    # Se inicia el bucle que permite detectar eventos
    root1.mainloop()

#
########

########
# Ejercicio 3
#

def pressedButton3(parent = None):
    """
    Parent solo se mantiene por compatibilidad.
    Asigna el cuadrado de la etiqueta entryBox1_12
    """

    # Para acceder a la etiqueta debe ser global
    global entryBox3_1
    global entryBox3_2
    global text3

    # Asigna a la etiqueta el cuadrado del número
    try:
        text3.set(eval(entryBox3_1.get()+"("+entryBox3_2.get()+")"))
    except:
        text3.set("Error")

def main3():
    """
    Añadir al ejercicio anterior una caja de texto para indicar la función que
    se quiere que se ejecute
    """

    global entryBox3_1
    global entryBox3_2
    global text3

    root3 = Tk()
    root3.geometry("200x100")

    # Se crea la caja de texto donde se escribe la función
    entryBox3_1 = Entry(root3, text="", width="10")
    entryBox3_1.grid(row=0, column=0)

    # Se crea la primera parte del mensaje
    label3_1 = Label(root3, text=" de ")
    label3_1.grid(row=0, column=1)

    # Se crea la caja de texto donde se escribe el número
    entryBox3_2 = Entry(root3, text="", width="10")
    entryBox3_2.grid(row=0, column=2)

    # Se le asigna el función que se va a ejecutar al pular el botón "Enter"
    entryBox3_1.bind("<Return>", pressedButton3)
    entryBox3_2.bind("<Return>", pressedButton3)

    # Siguiente parte del mensaje
    label3_2 = Label(root3, text=" es:")
    label3_2.grid(row=0, column=3)

    # Para mostrar el resultado es necesario utilizar StringVar
    text3 = StringVar()
    label3_3 = Label(root3, textvariable=text3)
    label3_3.grid(row=1, columnspan=4)

    # Se crea un botón donde se le indica la función que se ejecuta al pulsar
    # sobre él
    button3 = Button(root3, text="Enviar", command=pressedButton3)
    button3.grid(row=2, columnspan=4)

    # Se inicia el bucle que permite detectar eventos
    root3.mainloop()

#
########

########
# Ejercicio 4
#

def pressedEnter4(parent = None):
    """
    Muestra si es mayor o menor
    """

    # Para acceder a la etiqueta debe ser global
    global entryBox4
    global text4

    global randomNumber

    value4 = int(entryBox4.get())

    if randomNumber > value4:

        text4.set("El número "+str(value4)+" es menor")

    elif randomNumber < value4:

        text4.set("El número "+str(value4)+" es mayor")

    else:

        text4.set("¡Has acertado!")

        # Se crea un botón donde se le indica la función que se ejecuta al
        # pulsar sobre él
        button4 = Button(root4, text="Cerrar", command=pressedButton4)
        button4.grid(row=2, columnspan=2)

def pressedButton4():
    """
    Cierra la ventana creada
    """

    global root4

    root4.destroy()

def main4(min = 1, max = 100):
    """
    Adivinar el número generado. Cuando se adivine que aparezca un botón para
    cerrar la ventana
    """

    global root4

    global entryBox4
    global text4

    global randomNumber

    # Se crea el número aleatorio
    randomNumber = random.randint(min, max)

    root4 = Tk()
    root4.geometry("200x100")

    # Se crea la primera parte del mensaje
    label4_1 = Label(root4, text="Adivina el número: ")
    label4_1.grid(row=0, column=0)

    # Se crea la caja de texto donde se escribe el número
    entryBox4 = Entry(root4, text="", width="10")
    entryBox4.grid(row=0, column=1)

    # Se le asigna el función que se va a ejecutar al pular el botón "Enter"
    entryBox4.bind("<Return>", pressedEnter4)

    # Para mostrar el resultado es necesario utilizar StringVar
    text4 = StringVar()
    label4_2 = Label(root4, textvariable=text4)
    label4_2.grid(row=1, columnspan=2)

    # Se inicia el bucle que permite detectar eventos
    root4.mainloop()

#
########

#
################################################################################

################################################################################
# Ejecuciones
#

########
# Ejercicio 1-2
main12()

#
########

########
# Ejercicio 3
main3()

#
########

########
# Ejercicio 4
main4(1, 100)

#
########

#
################################################################################
