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

    def set_filename_test(self, filename):
        """
        Asigna el nombre de la plantilla de test
        """

        self.filename_test = filename

    def set_filename_tests(self, filename):
        """
        Asigna el nombre de los tests a corregir
        """

        self.filename_tests = filename

    def set_filename_result(self, filename):
        """
        Asigna el nombre del fichero xml con el resultado
        """

        self.filename_result = filename

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

    def load_test(self):
        """
        Carga la plantilla
        """

        res = False

        questions = []

        tree = ET.ElementTree()

        # Se cargan los datos
        tree.parse(self.filename_test)

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
                ans.append([text, per])

            questions.append([statement, score, ans])

        # Si hay preguntas, se guardan los datos y se devuelve True
        if len(questions) > 0:

            self.template = questions

            res = True

        return res

    def load_tests(self):
        """
        Carga los tests para corregir
        """

        res = False

        tests = []

        tree = ET.ElementTree()

        for filename in self.filename_tests:

            answers = []

            # Se cargan los datos
            tree.parse(filename)

            # Se recorren todas las preguntas
            for question in tree.findall("pregunta"):

                anss = question.find("respuestas")

                # Se crea el contenedor para las respuestas
                ans = []

                # Se recorren las respuestas
                for answer in anss.findall("respuesta"):

                    # Se añade a las respuestas
                    ans.append(answer.text)

                answers.append(ans)

            tests.append([filename[filename.rfind('/')+1:], answers])

        # Si hay preguntas, se guardan los datos y se devuelve True
        if len(tests) > 0:

            self.tests = tests

            res = True

        return res

    def save(self):
        """
        Guarda en el fichero xml los datos ya corregidos
        """

        # Se crea la raíz del fichero xml
        root = ET.Element("tests")

        for test in self.tests:

            # Se crea el nodo raíz de la pregunta
            t = ET.SubElement(root, "test")

            # Se crea el nodo con el nombre
            ET.SubElement(t, "nombre").text = test[0]

            # Se crea el nodo con la calificación del test
            ET.SubElement(t, "calificacion").text = str(test[3])

            questions = ET.SubElement(t, "preguntas")

            # Se recorren las respuestas
            for i, question in enumerate(test[1]):

                q = ET.SubElement(questions, "pregunta", numero=str(i+1))

                q.text = str(test[2][i][1])

                answers = ET.SubElement(q, "respuestas")

                for j, ans in enumerate(question):

                    ET.SubElement(answers, "respuesta", numero=str(ans)).text = str(test[2][i][0][j])


        tree = ET.ElementTree(root)

        return tree.write(self.filename_result)

    def correct(self):
        """
        Corrige las preguntas de los tests
        """

        # Se recorren los tests
        for test in self.tests:

            corrected_answers = []

            total = 0

            # Se recorren las respuestas
            for i, answers in enumerate(test[1]):

                # Contenedor donde se guardarán las puntuaciones
                scores = []

                # Se obtiene la puntuación de la pregunta
                score = int(self.template[i][1])

                # Se inicializa el contador a 0
                total_answer = 0

                # Se recorre cada respuesta
                for j, answer in enumerate(answers):

                    # Se calcula la puntuación que obtiene en esta pregunta
                    score_answer = score*int(self.template[i][2][int(answer)-1][1])/100

                    # Se suma al contador lo que se obtiene en la pregunta
                    # actual
                    total_answer += score_answer

                    scores.append(score_answer)

                # Se guarda la valoración de las respuestas
                corrected_answers.append((scores, total_answer))

                # Se añade el valor de la pregunta al total del examen
                total += total_answer

            test.append(corrected_answers)

            # Si el total es negativo, se establece a 0
            if total < 0:
                total = 0

            test.append(total)

            print(test)

        return True

    #
    ########

#
################################################################################
