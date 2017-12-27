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

            # Se añaden todas las respuestas
            for answer in question[2]:

                # Se crea el nodo donde se añade el texto
                ans = ET.SubElement(answers, "opcion")

                # Se añade el texto
                ET.SubElement(ans, "texto").text = answer[0]
                #ET.SubElement(ans, "valoracion").text = answer[1]

        tree = ET.ElementTree(root)

        return tree.write(self.filename.replace(".", "_"+self.test+".", -1))





















    def generate_data(self):
        """
        Genera el contenido de interés que se quiere obtener del fichero XML
        """

        # La fecha es la segunda etiqueta
        self.date = self.root.find("./elaborado").text.replace('T',' ')

        # La ciudad a la que pertenece es la segunda etiqueta
        self.city = self.root.find("./provincia").text

        # Las predicciones de los siguientes días son la quinta etiqueta.
        # Se obtienen las predicciones de todos los días
        self.predictions = self.generate_predictions( \
                                    self.root.findall("./prediccion/dia"))

    def generate_predictions(self, label_predicitions):
        """
        Obtiene la predicción de los siguientes 7 días
        """

        # Vector con las predicciones de los diferentes días
        predictions = dict()

        # Se recorren las etiquetas hijas de "prediccion"
        for pred in label_predicitions:

            # Cada día tendrá un diccionario con los valores correspondientes
            # a cada tipo de dato
            prediction = dict()

            # Se guarda la fecha de la predicción
            prediction['date'] = pred.attrib.get('fecha')

            # La probabilidad de precipitación puede aparecer en varios
            # intervalos, pero el que interesa es el primero que indica el
            # dia completo
            #prediction['rain'] = pred[0].text if pred[0].text is None else 0
            prediction['rain'] = pred[0].text if pred[0].text is not None else 0

            # Se guarda la dirección y velocidad del viento (en ese orden en la
            # tupla)
            wind = pred.find("./viento")
            prediction['wind'] = (wind[0].text if wind[0].text is not None \
                                        else "", \
                                    wind[1].text if wind[1].text is not None \
                                        else 0)

            # Se guarda la temperatura máxima y mínima (en ese orden en la
            # tupla)
            temperature = pred.find("./temperatura")
            prediction['temperature'] = (temperature.find("./maxima").text, \
                                            temperature.find("./minima").text)

            # Se guarda el diccionario de esta predicción en el contenedor de
            # todas las predicciones
            #predictions.append(prediction)

            predictions[prediction['date']] = prediction

        # Se devuelven las predicciones
        return predictions

    def to_string(self):
        """
        Devuelve el contenido del XML como un string
        """

        res = "Fecha: "+self.date
        res += "\nCiudad: "+self.city
        res += "\nPredicciones:\n"

        for prediction in self.predictions:

            res += "\t-Fecha: "+prediction['date']
            res += "\t-Lluvia (%): "+str(prediction['rain'])
            res += "\t-Viento (Dirección, Velocidad (km/h)): "+str(prediction['wind'])
            res += "\t-Temperatura (C): "+str(prediction['temperature'])

            res += "\n"

        return res

    #
    ########

#
################################################################################
