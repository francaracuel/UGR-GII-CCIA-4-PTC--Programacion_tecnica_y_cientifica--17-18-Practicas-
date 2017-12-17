# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programación Técnica y Científica

4º - GII - CCIA - ETSIIT - UGR

Curso 2017/2018

Práctica 1 - Gestión de datos metereológicos proporcionados por la AEMET

Clase Weather - Contiene toda la información del clima de un lugar

"""

# Se importan las clases necesarias para trabajar con los datos
from xml_aemet import *
from api_aemet import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

################################################################################
# Clase Weather
#
class Weather:
    """
    Contiene toda la información del clima de un lugar
    """

    ########
    # Constructor
    #
    def __init__(self, path = None, ext = None, code_xml = None, \
                    station_api = None, days = 7, year = 2017, \
                    create = True):
        """
        Inicializa los objetos Xml_Aemet y Api_Aemet con los códigos necesarios
        de la zona de la que se quiere obtener información.
        path contiene la ruta donde se encuentran los ficheros que se necesitan.
        ext contiene la extensión de las imágenes que se generan con las
        gráficas.
        code_xml tiene el código de la ciudad de la que se quiere obtener la
        información.
        station_api es el nombre de la estación de la que se saca la información
        de la Api.
        create indica si se deben importar los datos del xml y api o si se
        deja todo vacío
        """

        # Si se debe cargar el contenido del xml y la api
        if create:

            # Ruta donde están los ficheros
            self.path = path

            # Extensión de las imágenes que se generan
            self.ext = ext

            # Se obtiene el objeto que gestiona la información del xml
            xml = Xml_Aemet(code_xml)

            # Se obtiene el objeto que gestiona la Api
            api = Api_Aemet(station_api, days = days, year = year)

            # Se carga la información del xml
            self.load_xml(xml)

            # Se carga la información de la Api
            self.load_api(api)

            # Se aumenta el tamaño de las gráficas que se generan
            fig_size = plt.rcParams["figure.figsize"]

            fig_size[0] = fig_size[0]*2
            fig_size[1] = fig_size[1]*1.2

            plt.rcParams["figure.figsize"] = fig_size

    #
    ########

    ########
    # Getters
    #

    def get_city(self):
        """
        Devuelve la ciudad
        """

        return self.city

    def get_date(self):
        """
        Devuelve la fecha de los datos
        """

        return self.date

    def get_predictions(self):
        """
        Devuelve las predicciones
        """

        return self.predictions

    def get_all_predictions(self):
        """
        Devuelve el histórico de predicciones
        """

        return self.all_predictions

    def get_current(self):
        """
        Devuelve los datos actuales
        """

        return self.current

    def get_last_days(self):
        """
        Devuelve los datos de los últimos días
        """

        return self.last_days

    def get_year(self):
        """
        Devuelve los datos del año
        """

        return self.year

    def get_months(self):
        """
        Devuelve una lista con los meses del año en español
        """

        months = []

        months.append("Enero")
        months.append("Febrero")
        months.append("Marzo")
        months.append("Abril")
        months.append("Mayo")
        months.append("Junio")
        months.append("Julio")
        months.append("Agosto")
        months.append("Septiembre")
        months.append("Octubre")
        months.append("Noviembre")
        months.append("Diciembre")

        return months

    #
    ########

    ########
    # Setters
    #

    #
    ########

    ########
    # Utils
    #

    def load_xml(self, xml):
        """
        Guarda en las variables de la clase la información que se puede obtener
        del xml de Aemet
        """

        # Se obtiene la ciudad
        self.city = xml.get_city()

        # Se guarda la fecha
        #self.date = xml.get_date()

        # Se guardan las predicciones
        self.predictions = xml.get_predictions()

        # También se guardan las predicciones en el almacén de predicciones
        self.all_predictions = self.predictions

    def load_api(self, api):
        """
        Guarda en las variables de la clase la información que se puede obtener
        de la Api de Aemet
        """

        # Se obtienen todos los datos del clima
        data = api.get_weather()

        # Se guardan los datos actuales del clima
        self.current = data['current']

        self.date = self.current['date']

        # Se guarda el tiempo de los últimos "days"
        self.last_days = data['last']

        # Se guardan los datos de los meses del año
        self.year = data['year']

    def update_predictions(self, predictions):
        """
        Añade al almacén de predicciones, todas las predicciones que recibe
        por parámetro
        """

        # Método no muy elegante de hacerlo, pero sin tiempo para comprobar
        # por qué los métodos eficientes no funcionan

        # Se recorren las predicciones del xml
        for key,value in self.all_predictions.items():

            predictions[key] = value

        self.all_predictions = predictions


    def create_chart_predictions_temperature(self, t = "", xl = "", yl = "", \
                    label_max = "", label_min = "", \
                    filename = "predictions_temperature", grid = True, \
                    legend = True, show = False):
        """
        Genera la gráfica de las predicciones de la temperatura de los
        próximos días
        """

        # Se guarda una lista con cada elemento del diccionario
        predictions = [prediction for key, prediction in \
                                                self.predictions.items()]

        # Se obtiene una lista con la fecha de las predicciones
        dates = [prediction['date'] for prediction in predictions]

        # Se obtiene una lista con las temperaturas máximas de cada día
        max_temperatures = [int(prediction['temperature'][0]) for prediction \
                                                        in predictions]

        # Se obtiene una lista con las temperaturas mínimas de cada día
        min_temperatures = [int(prediction['temperature'][1]) for prediction \
                                                        in predictions]

        # Se pintan las temperaturas máximas
        plt.plot(dates, max_temperatures, label=label_max, color='#b30000')

        # Se pintan las temperaturas mínimas
        plt.plot(dates, min_temperatures, label=label_min, color="#1e90ff")

        # Se indica el título de la gráfica
        plt.title(t)

        # Se indica el título del eje X
        plt.xlabel(xl)

        # Se indica el título del eje Y
        plt.ylabel(yl)

        # Se muestra la rejilla
        if grid:
            plt.grid(True)

        # Se habilita la leyenda
        if legend:
            plt.legend()

        # Se guarda la gráfica en un fichero
        plt.savefig(self.path+filename+self.ext)

        # Comprueba si debe mostrar la gráfica en la ejecución o no
        if show:
            plt.show()

        # Se limpia la imagen
        plt.clf()

    def create_chart_predictions_rain(self, t = "", xl = "", yl = "", \
                    filename = "predictions_rain", grid = True, \
                    legend = True, show = False):
        """
        Genera la gráfica de las probabilidades de lluvia en los próximos días
        """

        # Se guarda una lista con cada elemento del diccionario
        predictions = [prediction for key, prediction in \
                                                self.predictions.items()]

        # Se obtiene una lista con la fecha de las predicciones
        dates = [prediction['date'] for prediction in predictions]

        # Se obtiene una lista con la probabilidad de lluvia de cada día
        max_temperatures = [int(prediction['rain']) for prediction \
                                                        in predictions]

        # Se pintan las probabilidades de lluvia
        plt.plot(dates, max_temperatures, color='#5a5a5a')

        # Se indica el título de la gráfica
        plt.title(t)

        # Se indica el título del eje X
        plt.xlabel(xl)

        # Se indica el título del eje Y
        plt.ylabel(yl)

        # Se muestra la rejilla
        if grid:
            plt.grid(True)

        # Se habilita la leyenda
        if legend:
            plt.legend()

        # Se guarda la gráfica en un fichero
        plt.savefig(self.path+filename+self.ext)

        # Comprueba si debe mostrar la gráfica en la ejecución o no
        if show:
            plt.show()

        # Se limpia la imagen
        plt.clf()

    def create_chart_predictions_wind(self, t = "", xl = "", yl = "",
                    filename = "predictions_wind", grid = True, \
                    legend = True, show = False):
        """
        Genera la gráfica de la velocidad del viento en los próximos días
        """

        # Se guarda una lista con cada elemento del diccionario
        predictions = [prediction for key, prediction in \
                                                self.predictions.items()]

        # Se obtiene una lista con la fecha de las predicciones
        dates = [prediction['date'] for prediction in predictions]

        # Se obtiene una lista con la dirección del viento de cada día
        orientations = [prediction['wind'][0] for prediction \
                                                        in predictions]

        # Se obtiene una lista con la velocidad del viento de cada día
        speeds = [int(prediction['wind'][1]) for prediction \
                                                        in predictions]



        # Se pintan las probabilidades de lluvia
        plt.plot(dates, speeds, color='#95e995')

        # Se hacen anotaciones con la dirección del viento
        for i, speed in enumerate(speeds):

            # Solo se mostrarán si existe etiqueta o no es "C"
            if orientations[i] is not None and orientations[i] != "C":
                plt.annotate(xy=[i,speed], s=orientations[i])

        # Se indica el título de la gráfica
        plt.title(t)

        # Se indica el título del eje X
        plt.xlabel(xl)

        # Se indica el título del eje Y
        plt.ylabel(yl)

        # Se muestra la rejilla
        if grid:
            plt.grid(True)

        # Se habilita la leyenda
        if legend:
            plt.legend()

        # Se guarda la gráfica en un fichero
        plt.savefig(self.path+filename+self.ext)

        # Comprueba si debe mostrar la gráfica en la ejecución o no
        if show:
            plt.show()

        # Se limpia la imagen
        plt.clf()

    def create_chart_year_sun(self, t = "", xl = "", yl = "", \
                    filename = "year_sun", grid = True, \
                    legend = True, show = False):
        """
        Genera la gráfica con el porcentaje de días con sol al mes
        """

        # Se obtiene una lista con los meses del año
        months_labels = self.get_months()

        #for i in range(0, len(months)):
        #   months[i] = str(i+1)+" - "+months[i]

        months = range(1, 13)

        # Se obtiene una lista con los días de sol de cada mes
        sun = [float(month['sun']) for month in self.year[0]]

        # Puede que haya menos registros que meses tiene el año. En ese caso
        # se rellenan
        diff = len(months)-len(sun)

        for i in range(0, diff):
            sun.append(0)

        plt.xticks(months, months_labels)

        # Se pintan los días de sol
        plt.bar(months, sun, color='#ebeb00')

        # Se indica el título de la gráfica
        plt.title(t)

        # Se indica el título del eje X
        plt.xlabel(xl)

        # Se indica el título del eje Y
        plt.ylabel(yl)

        # Se muestra la rejilla
        if grid:
            plt.grid(True)

        # Se habilita la leyenda
        if legend:
            plt.legend()

        # Se guarda la gráfica en un fichero
        plt.savefig(self.path+filename+self.ext)

        # Comprueba si debe mostrar la gráfica en la ejecución o no
        if show:
            plt.show()

        # Se limpia la imagen
        plt.clf()

    def create_chart_last_temperature(self, t = "", xl = "", yl = "", \
                    filename = "last_temperature", grid = True, \
                    legend = True, show = False, \
                    xlabel = "", ylabel = "", zlabel = ""):
        """
        Genera la gráfica con el porcentaje de días con sol al mes
        """

        # Se obtiene una lista con las fechas
        dates = [day['date'] for day in self.last_days]

        # Se obtiene una lista con la temperatura media
        temp_avg = [day['temp_avg'] for day in self.last_days]

        # Se obtiene una lista con la temperatura mínima
        temp_min = [day['temp_min'] for day in self.last_days]

        # Se obtiene una lista con la temperatura máxima
        temp_max = [day['temp_max'] for day in self.last_days]

        # Se crea una lista con las 3 temperaturas
        temp = []

        temp.append(temp_min)
        temp.append(temp_avg)
        temp.append(temp_max)

        # Se crea una lista con las etiquetas de las temperaturas
        temp_label = []

        temp_label.append("Temperatura mínima")
        temp_label.append("Temperatura media")
        temp_label.append("Temperatura máxima")

        # Se crea un objeto para guardar la gráfica
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Se crea una lista para guardar los colores de la temperatura
        colour = []

        # Color para la temperatura mínima
        colour.append("#1e90ff")

        # Color para la temperatura media
        colour.append("#696969")

        # Color para la temperatura máxima
        colour.append("#b30000")

        # El eje x tendrá tantos valores como días tiene la predicción
        xs = np.arange(len(dates))

        # Se pintan las distintas temperaturas
        for z in range(0, 3):

            # El eje y tiene las temperaturas
            ys = temp[z]

            # Se pintan las barras
            ax.bar(xs, ys, zs=z+1, color = colour[z], zdir='y', alpha=0.8)

        # Se indica el título de la gráfica
        plt.title(t)

        # Se indican los títulos
        #ax.set_xlabel(xlabel)
        #ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)

        plt.xticks(xs, dates)
        plt.yticks(range(1, 4), temp_label)

        # Se muestra la rejilla
        if grid:
            plt.grid(True)

        # Se habilita la leyenda
        if legend:
            plt.legend()

        # Se guarda la gráfica en un fichero
        plt.savefig(self.path+filename+self.ext)

        # Comprueba si debe mostrar la gráfica en la ejecución o no
        if show:
            plt.show()

        # Se limpia la imagen
        plt.clf()

    def create_chart_compare_predictions_temperature(self, t = "", xl = "", \
                    yl = "", label_max = "", label_min = "", \
                    filename = "compare_predictions_temperature", grid = True, \
                    legend = True, show = False):
        """
        Genera la gráfica donde compara las temperaturas que se predijeron y
        las reales
        """

        dates = []

        real = []
        pred = []

        for value in self.last_days:

            if value['date'] in self.all_predictions:

                dates.append(value['date'])

                real.append(value)
                pred.append(self.all_predictions.get(value['date']))

        # Se obtiene una lista con las temperaturas máximas reales
        max_temperatures_real = [int(prediction['temp_max']) for prediction \
                                                        in real]

        # Se obtiene una lista con las temperaturas mínimas reales
        min_temperatures_real = [int(prediction['temp_min']) for prediction \
                                                        in real]

        # Se obtiene una lista con las temperaturas máximas de las predicciones
        max_temperatures_pred = [int(prediction['temperature'][0]) for prediction \
                                                        in pred]

        # Se obtiene una lista con las temperaturas mínimas de las predicciones
        min_temperatures_pred = [int(prediction['temperature'][1]) for prediction \
                                                        in pred]

        # Se pintan las temperaturas máximas reales
        plt.plot(dates, max_temperatures_real, label=label_max+" reales", color='#ff0000')

        # Se pintan las temperaturas mínimas reales
        plt.plot(dates, min_temperatures_real, label=label_min+" reales", color="#00bfff")

        # Se pintan las temperaturas máximas de las predicciones
        plt.plot(dates, max_temperatures_pred, label=label_max+" predichos", color='#b30000')

        # Se pintan las temperaturas mínimas de las predicciones
        plt.plot(dates, min_temperatures_pred, label=label_min+" predichos", color="#00008b")

        # Se indica el título de la gráfica
        plt.title(t)

        # Se indica el título del eje X
        plt.xlabel(xl)

        # Se indica el título del eje Y
        plt.ylabel(yl)

        # Se muestra la rejilla
        if grid:
            plt.grid(True)

        # Se habilita la leyenda
        if legend:
            plt.legend()

        # Se guarda la gráfica en un fichero
        plt.savefig(self.path+filename+self.ext)

        # Comprueba si debe mostrar la gráfica en la ejecución o no
        if show:
            plt.show()

        # Se limpia la imagen
        plt.clf()

    def to_string(self):
        """
        Devuelve los datos de la clase como un string
        """

        res = ""

        return res

    #
    ########

#
################################################################################
