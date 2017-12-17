# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programación Técnica y Científica

4º - GII - CCIA - ETSIIT - UGR

Curso 2017/2018

Práctica 1 - Gestión de datos metereológicos proporcionados por la AEMET

main.py - Fichero principal desde donde se gestiona todo el contenido

"""

if __name__ == "__main__":

    ########
    #

    # Se importan las clases necesarias para trabajar con los datos
    from weather import *
    from html_weather import *
    from file_class import *
    import os

    #
    ########

    ########
    # Inicialización de los parámetros necesarios

    # Ruta donde se guardan y se cargan los archivos necesarios
    path = "data/"

    # Extensión en el que se guardan las imágenes
    ext = ".svg"

    # Código postal de la ciudad de la que se quieren obtener los datos
    code_xml = 18015

    # Estación sobre la que se quieren obtener los datos
    station_api = "GRANADA/AEROPUERTO"

    # Nombre del fichero html
    filename_html = "output.html"

    # Nombre del fichero que guarda el contenido de la clase
    filename_weather = "weather.pkl"

    #
    ########

    ########
    # Ejecución
    #

    # Se crea el objeto que se encarga de cargar y guarda la clase en un fichero
    file_class = File_Class()

    # Se crea el objeto que contiene los datos del clima
    weather = Weather(path, ext, code_xml, station_api)

    # Si existe el fichero con los datos, se carga y se actualizan las
    # predicciones
    if os.path.isfile(path+filename_weather):

        # Se carga el objeto del fichero
        weather2 = file_class.load(path+filename_weather)

        # Se añaden las predicciones pasadas en el nuevo objeto
        weather.update_predictions(weather2.get_all_predictions())

    else:

        ########################################################################
        # Como se necesita ejecutar todos los días el proyecto y no ha habido
        # tiempo suficiente, se añaden predicciones inventadas de días
        # anteriores para hacer la comprobación.
        # A partir del día de hoy, si se ejecuta todos los días el programa, se
        # actualizarán con los tiempos reales.
        #

        new_predictions = {'2017-12-16': {'date': '2017-12-16', 'rain': 0, 'wind': ('', 0), 'temperature': ('7', '-2')}, \
        '2017-12-15': {'date': '2017-12-15', 'rain': '0', 'wind': ('C', '0'), 'temperature': ('9', '-2')}, '2017-12-14': {'date': \
        '2017-12-14', 'rain': '0', 'wind': ('E', '5'), 'temperature': ('10', '0')}, '2017-12-13': {'date': '2017-12-13', 'rain': \
        '0', 'wind': ('NO', '5'), 'temperature': ('11', '-1')}, '2017-12-12': {'date': '2017-12-12', 'rain': '0', 'wind': ('E', \
        '10'), 'temperature': ('11', '0')}, '2017-12-11': {'date': '2017-12-11', 'rain': '0', 'wind': ('NO', '5'), 'temperature': \
        ('11', '-1')}, '2017-12-10': {'date': '2017-12-10', 'rain': '5', 'wind': ('C', '0'), 'temperature': ('13', '1')}, \
        '2017-12-09': {'date': '2017-12-09', 'rain': '0', 'wind': ('C', '0'), 'temperature': ('9', '-2')}, '2017-12-08': {'date': \
        '2017-12-08', 'rain': '0', 'wind': ('E', '5'), 'temperature': ('10', '0')}, '2017-12-07': {'date': '2017-12-07', 'rain': \
        '0', 'wind': ('NO', '5'), 'temperature': ('11', '-1')}, '2017-12-06': {'date': '2017-12-06', 'rain': '0', 'wind': ('E', \
        '10'), 'temperature': ('11', '0')}, '2017-12-05': {'date': '2017-12-05', 'rain': '0', 'wind': ('NO', '5'), 'temperature': \
        ('11', '-1')}, '2017-12-04': {'date': '2017-12-04', 'rain': '5', 'wind': ('C', '0'), 'temperature': ('13', '1')}}

        weather.update_predictions(new_predictions)

        #file_class.save(weather, path+filename_weather)

        #
        ############################################################################

    # Se guarda el objeto en el fichero con las nuevas predicciones
    file_class.save(weather, path+filename_weather)

    # Se crea el objeto que crea el contenido HTML
    html = Html_Weather(weather, path, filename_html)

    # Se genera el código HTML
    html.gen_all()

    # Se guarda el contenido HTML en el fichero de salida
    html.export_html()

    #
    ########
