# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programación Técnica y Científica

4º - GII - CCIA - ETSIIT - UGR

Curso 2017/2018

Práctica 2 - Gestión de test - Realización del test

Clase Xml - Clase que gestiona la realización de los tests, cargando las
preguntas y respuestas de un fichero xml

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

        # Indica la extensión del test contestado
        self.ext = "done"

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

        self.tree = ET.ElementTree()

        # Se cargan los datos
        self.tree.parse(self.filename)

        # Se recorren todas las preguntas
        for question in self.tree.findall("pregunta"):

            # Se guarda la pregunta y la puntuación
            statement = question.find("enunciado").text
            question_type = question.find("tipo").text

            answers = question.find("opciones")

            # Se crea el contenedor para las respuestas
            ans = []

            # Se recorren las respuestas
            for answer in answers.findall("opcion"):

                # Se guarda la respuesta y su porcentaje
                text = answer.find("texto").text

                # Se añade a las respuestas
                ans.append((text))

            questions.append((statement, question_type, ans))

        # Si hay preguntas, se guardan los datos y se devuelve True
        if len(questions) > 0:

            self.data = questions

            res = True

        return res

    def save(self):
        """
        Guarda en el fichero xml las preguntas y respuestas recibidas para
        corregir el test
        """

        for i, question in enumerate(self.tree.iter('pregunta')):

            q = ET.SubElement(question, "respuestas")

            for answer in self.data[i]:

                if answer > 0:
                    ET.SubElement(q, "respuesta").text = str(answer)

        return self.tree.write(self.filename.replace(".", "_"+self.ext+".", -1))

    #
    ########

#
################################################################################
