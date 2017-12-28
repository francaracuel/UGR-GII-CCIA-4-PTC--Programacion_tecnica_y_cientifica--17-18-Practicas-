# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programación Técnica y Científica

4º - GII - CCIA - ETSIIT - UGR

Curso 2017/2018

Práctica 2 - Gestión de test - Creación del test

Clase Xml - Clase que gestiona la carga o guardado de preguntas y respuestas en
un fichero xml

"""

import xml.etree.ElementTree as ET

################################################################################
# Clase Xml
#
class Xml:
    """
    Gestiona la carga o guardado de preguntas y respuestas en un fichero xml
    """

    ########
    # Constructor
    #
    def __init__(self, filename = None, data = None):
        """
        Inicializa todos los elementos necesarios para que se pueda guardar o
        cargar la información del fichero xml para crear tests
        """

        # Indica la extensión del test para la corrección
        self.correction = "correction"

        # Indica la extensión del test para el alumno
        self.test = "test"

    #
    ########

    ########
    # Getters
    #

    def get_data(self):
        """
        Devuelve los datos
        """

        return self.data

    #
    ########

    ########
    # Setters
    #

    def set_filename(self, filename):
        """
        Asigna el nombre del fichero que se va a utilizar para guardar los
        datos
        """

        self.filename = filename

    def set_data(self, data):
        """
        Asigna los datos que se van a guardar en el fichero xml
        """

        self.data = data

    #
    ########

    ########
    # Utils
    #

    def load(self):
        """
        Carga del fichero xml la estructura con las preguntas y respuestas
        """

        res = False

        questions = []

        tree = ET.ElementTree()

        # Se cargan los datos
        tree.parse(self.filename)

        # Se recorren todas las preguntas
        for question in tree.findall("pregunta"):

            # Se guarda la pregunta y la puntuación
            statement = question.find("enunciado").text
            score = question.find("puntuacion").text

            answers = question.find("opciones")

            # Se crea el contenedor para las respuestas
            ans = []

            # Se recorren las respuestas
            for answer in answers.findall("opcion"):

                # Se guarda la respuesta y su porcentaje
                text = answer.find("texto").text
                per = answer.find("valoracion").text

                # Se añade a las respuestas
                ans.append((text, per))

            questions.append((statement, score, ans))

        # Si hay preguntas, se guardan los datos y se devuelve True
        if len(questions) > 0:

            self.data = questions

            res = True

        return res

    def save(self):
        """
        Guarda en los ficheros correspondientes los xml para contestar y
        corregir el test
        """

        return self.save_correction() or self.save_test()

    def save_correction(self):
        """
        Guarda en el fichero xml las preguntas y respuestas recibidas para
        corregir el test
        """

        # Se crea la raíz del fichero xml
        root = ET.Element("preguntas")

        for i, question in enumerate(self.data):

            # Se crea el nodo raíz de la pregunta
            q = ET.SubElement(root, "pregunta", id=str(i+1))

            # Se crea el nodo con el enunciado
            statement = ET.SubElement(q, "enunciado").text = question[0]

            # Se crea el nodo con la puntuación
            score = ET.SubElement(q, "puntuacion").text = question[1]

            # Se crea el nodo que contendrá las respuestas
            answers = ET.SubElement(q, "opciones")

            # Se añaden todas las respuestas
            for answer in question[2]:

                # Se crea el nodo donde se añade el texto y su valoración
                ans = ET.SubElement(answers, "opcion")

                # Se añade el texto y la valoración
                ET.SubElement(ans, "texto").text = answer[0]
                ET.SubElement(ans, "valoracion").text = answer[1]

        tree = ET.ElementTree(root)

        return tree.write(self.filename.replace(".", "_"+self.correction+".", \
                                                                        -1))

    def save_test(self):
        """
        Guarda en el fichero xml las preguntas y respuestas recibidas para
        contestar el test
        """

        # Se crea la raíz del fichero xml
        root = ET.Element("preguntas")

        for i, question in enumerate(self.data):

            # Se crea el nodo raíz de la pregunta
            q = ET.SubElement(root, "pregunta", id=str(i+1))

            # Se crea el nodo con el enunciado
            statement = ET.SubElement(q, "enunciado").text = question[0]

            # Se crea el nodo con la puntuación
            #score = ET.SubElement(q, "puntuacion").text = question[1]

            # Se crea el nodo que contendrá las respuestas
            answers = ET.SubElement(q, "opciones")

            # Se guarda el tipo de pregunta:
            # 0: penalizado (un error resta puntuación)
            # 1: no penalizado (un error no resta puntuación)
            # 2: varias válidas (hay que marcar varias opciones)
            question_type = -1

            # Se añaden todas las respuestas
            for answer in question[2]:

                # Se crea el nodo donde se añade el texto
                ans = ET.SubElement(answers, "opcion")

                # Se añade el texto
                ET.SubElement(ans, "texto").text = answer[0]
                #ET.SubElement(ans, "valoracion").text = answer[1]

                # Se comprueba el tipo de la pregunta
                if question_type == -1:

                    # Si la respuesta está comprendida en (0, 100), el tipo
                    # es "varias válidas"
                    if int(answer[1]) > 0 and int(answer[1]) < 100:
                        question_type = 2

                    # Si hay alguna respuesta con un valor negativo, el tipo
                    # es "penalizado"
                    elif int(answer[1]) < 0:
                        question_type = 0

                    # Si la respuesta tiene la puntuación máxima puede ser "no
                    # penalizado", aunque se debe hacer comprobaciones para
                    # comprobar que no sea "penalizado"
                    elif int(answer[1]) == 100:
                        question_type = 1

                # Solo si el tipo es "penalizado" hay que comprobar si puede
                # ser "no-penalizado"
                if question_type == 1 and int(answer[1]) < 0:
                    question_type = 0

            # Se crea una especie de switch/case equivalente en Python
            switcher = {
                0: "penalizado",
                1: "no-penalizado",
                2: "varias-validas"
            }

            # Se añade al fichero xml
            ET.SubElement(q, "tipo").text = switcher.get(question_type)

        tree = ET.ElementTree(root)

        return tree.write(self.filename.replace(".", "_"+self.test+".", -1))

    #
    ########

#
################################################################################
