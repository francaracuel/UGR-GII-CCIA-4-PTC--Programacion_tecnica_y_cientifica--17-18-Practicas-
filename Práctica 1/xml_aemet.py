# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programación Técnica y Científica

4º - GII - CCIA - ETSIIT - UGR

Curso 2017/2018

Práctica 1 - Gestión de datos metereológicos proporcionados por la AEMET

Clase Xml_Aemet - Clase que obtiene un fichero XML de aemet.es y gestiona su
contenido

"""

import xml.etree.ElementTree as ET
import urllib.request as urllib

################################################################################
# Clase Xml_Aemet
#
class Xml_Aemet:
    """
    Gestiona los datos obtenidos del fichero XML de aemet.es
    """

    ########
    # Constructor
    #
    def __init__(self, code):
        """
        Constructor que carga un fichero xml dependiendo del código de la ciudad
        recibido
        """

        # Se intenta leer
        #try:

        self.url = "http://www.aemet.es/xml/municipios/localidad_"+ \
                        str(code)+".xml"

        self.tree = ET.ElementTree(file=urllib.urlopen(self.url))

        self.root = self.tree.getroot()

        #self.error = False

        self.generate_data()

        #except urllib2.HTTPError:

            #self.error = True

    #
    ########

    ########
    # Getters
    #

    def get_date(self):
        """
        Devuelve la fecha en la que se ha creado el fichero XML
        """

        return self.date

    def get_city(self):
        """
        Devuelve la ciudad de la que se muestran los datos
        """

        return self.city

    def get_predictions(self):
        """
        Devuelve las predicciones de los 7 siguientes días (incluyendo el
        actual)
        """

        return self.predictions

    def get_data(self):
        """
        Devuelve toda la información del fichero xml
        """

        data = []

        data.append(self.get_date())
        data.append(self.get_city())
        data.append(self.get_predictions())

        return data

    #
    ########

    ########
    # Utils
    #

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
