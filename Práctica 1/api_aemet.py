# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programación Técnica y Científica

4º - GII - CCIA - ETSIIT - UGR

Curso 2017/2018

Práctica 1 - Gestión de datos metereológicos proporcionados por la AEMET

Clase Api_Aemet - Clase que se comunica con la Api de aemet.es

"""

# Se utiliza la información de este post de stackoverflow.com para corregir
# los errores en la conexión con la api
# https://es.stackoverflow.com/questions/63842/aemet-opendata-api-no-devuelve-body

import ssl
from http import client
import json
import time
from datetime import datetime, timedelta

################################################################################
# Clase Api_Aemet
#
class Api_Aemet:
    """
    Gestiona los datos obtenidos de la Api de aemet.es
    """

    ########
    # Constructor
    #
    def __init__(self, station, date_start = None, date_end = None, days = 0, year = 2017):
        """
        Inicializa los componentes necesarios para cominacrse con la Api
        """

        # Api key utilizada para obtener la información de la Api
        self.api_key = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmcmFuajkwY2JAZ21haWwuY29tIiwianRpIjoiYzI0YjllYTctYjE0Mi00MTUxLTgzYWQtOTQ1NTBkNTljYzFmIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE1MTMzNzIxNjIsInVzZXJJZCI6ImMyNGI5ZWE3LWIxNDItNDE1MS04M2FkLTk0NTUwZDU5Y2MxZiIsInJvbGUiOiIifQ.DEZ9prfyTHZVLy_Otbq4BmcjylKCDsgX0pcNcoQQz9A"

        # Url donde se encuentra la api
        url = "opendata.aemet.es"

        # Se inicializa la conexión a la Api
        self.init_conn(url)

        # Se obtiene el idema de la estación
        self.idema = self.get_idema(station)

        # Se establecen las fechas sobre la que se hace la petición
        self.set_dates(date_start, date_end, days = days)

        # Se generan los datos del clima de la estación
        self.generate_data(year = year)

    def init_conn(self, url):
        """
        Inicializador de la conexión a la api
        """

        # Al hacer las peticiones desde un "servidor" que no contiene un
        # certificado SSL y utilizar el protocolo seguro HTTPS, da un error de
        # seguridad. Se debe indicar que no se utiliza una petición segura.
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        # Conexión que se realiza con cada petición
        self.conn = client.HTTPSConnection(url, context=context)

        # Cabeceras necesarias para enviar la petición
        self.headers = {
            'cache-control': "no-cache"
        }

    #
    ########

    ########
    # Getters
    #

    def get_idemas(self):
        """
        Devuelve un listado con todos los posibles idemas que se pueden utilizar
        y la zona que les corresponde
        """

        query = "/api/observacion/convencional/todas"

        data = self.exec_query(query, reconn = True)

        return {station['ubi']:station['idema'] for station in data}

    def get_idema(self, station):
        """
        Devuelve el idema de una estación que recibe por parámetro
        """

        return self.get_idemas()[station]

    def get_weather(self):
        """
        Devuelve el tiempo de la estación
        """

        return self.weather

    def get_current(self):
        """
        Devuelve los datos actuales de la estación
        """

        query = "/api/observacion/convencional/datos/estacion/"+self.idema

        return self.exec_query(query)

    def get_last(self, date_start = None, date_end = None):
        """
        Devuelve el tiempo que ha ocurrido en el intervalo de tiempo establecido
        o en los últimos días
        """

        if date_start is None:
            date_start = self.date_start

        if date_end is None:
            date_end = self.date_end

        query = "/api/valores/climatologicos/diarios/datos/fechaini/"+ \
        date_start+"/fechafin/"+date_end+"/estacion/"+self.idema

        return self.exec_query(query)

    def get_year(self, year):
        """
        Devuelve los datos del año que se recibe por parámetro
        """

        year = str(year)

        query = "/api/valores/climatologicos/mensualesanuales/datos/anioini/"+ \
                    year+"/aniofin/"+year+"/estacion/"+self.idema

        return self.exec_query(query)

    #
    ########

    ########
    # Setters
    #

    def set_dates(self, date_start = None, date_end = None, days = 0, \
                    margin = 4):
        """
        Guarda las fechas con el intervalo sobre el que se quiere hacer la
        consulta.
        date_start contiene la fecha de inicio del intervalo.
        date_end contiene la fecha de fin del intervalo.
        days contiene el número de días que se le suma a la fecha de inicio en
        caso de que no exista la fecha final.
        days contiene el número de días que se le resta a la fecha de fin en
        caso de que no exista la fecha inicial.
        margin indica el último día en el que hay registros contando el día
        actual.
        """

        # Si no se recibe la fecha de inicio ni la fecha de fin, la fecha de
        # fin será el día de hoy (-4 días) y la fecha de inicio la que indique
        # la variable days
        if date_start is None and date_end is None:
            date_end = datetime.today() - timedelta(days=margin)

        # Si no se tiene fecha de inicio, será la fecha final menos el número de
        # días indicado en "days"
        if date_start is None and date_end is not None:
            date_start = date_end - timedelta(days=days)

        # Si se tiene fecha de inicio pero no de fin, se suman los días que
        # aparecen en "days" a la fecha final
        if date_start is not None and date_end is None:
            date_end = date_start + timedelta(days=days)

        # Formato que debe tener la fecha para que funcione:
        # "2017-12-10T00:00:00UTC", "2017-12-16T23:59:59UTC"
        self.date_start = str(date_start.year)+"-"+ str(date_start.month)+"-"+ \
             str(date_start.day)+"T00:00:00UTC"

        self.date_end =  str(date_end.year)+"-"+ str(date_end.month)+"-"+ \
             str(date_end.day)+"T00:00:00UTC"

    #
    ########

    ########
    # Utils
    #

    def generate_data(self, date_start = None, date_end = None, year = 2017):
        """
        Genera los datos de la estación en un intervalo definido por
        "date_start" y "date_end"
        """

        # Se crea un diccionario que contendrá todos los climas de los días que
        # se reciben
        self.weather = dict()

        # Se generan los datos del momento actual
        self.weather['current'] = self.generate_current()

        # Se generan los datos del momento actual
        self.weather['last'] = self.generate_last_days(date_start, date_end)

        # Se generan los datos del año completo
        self.weather['year'] = self.generate_year(y = year)

    def generate_current(self):
        """
        Genera la información relevante del momento actual
        """

        # Se obtienen los últimos datos actuales
        data = self.get_current()[-1]

        # Se guardarán los datos en un diccionario
        current = dict()

        # Fecha de actualización
        current['date'] = data['fint'].replace('T',' ')+" UTC"

        # Precipitación acumulada en la última hora
        current['rain'] = data['prec']

        # Velocidad máxima del viento en (m/s)
        current['wind_max'] = data['vmax']

        # Velocidad media del viento (m/s)
        current['wind_avg'] = data['vv']

        # Dirección media del viento (º)
        current['wind_dir'] = data['dv']

        # Presión instantánea (hPa)
        current['pressure'] = data['pres']

        # Humedad relativa en el aire (%)
        current['humidity'] = data['hr']

        # Temperatura en el suelo (ºC)
        current['temp_floor'] = data['ts']

        # Temperatura mínima (ºC)
        current['temp_min'] = data['tamin']

        # Temperatura (ºC)
        current['temp_current'] = data['ta']

        # Temperatura máxima (ºC)
        current['temp_max'] = data['tamax']

        # Temperatura del punto de rocío (ºC)
        current['temp_dew'] = data['tpr']

        # Visibilidad (km)
        current['visibility'] = data['vis']

        return current

    def generate_last_days(self, date_start = None, date_end = None):
        """
        Genera la información que ha ocurrido en un período de tiempo
        """

        # Se obtienen los datos de los últimos días
        data = self.get_last(date_start, date_end)

        # Se guardan todos los días pasados
        last_days = []

        # Se recorren todos los días
        for day_aux in data:

            # Se crea un diccionario donde se irán guardando los datos
            day = dict()

            # Fecha de los datos
            day['date'] = day_aux['fecha'].replace('T',' ')

            # Temperatura media (ºC)
            day['temp_avg'] = float(day_aux['tmed'].replace(',','.'))

            # Temperatura mínima (ºC)
            day['temp_min'] = float(day_aux['tmin'].replace(',','.'))

            # Hora de la temperatura mínima
            day['time_temp_min'] = day_aux['horatmin']

            # Temperatura máxima (ºC)
            day['temp_max'] = float(day_aux['tmax'].replace(',','.'))

            # Hora de la temperatura máxima
            day['time_temp_max'] = day_aux['horatmax']

            # Precipitaciones (mm)
            day['rain'] = day_aux['prec']

            # Velocidad media del viento (m/s)
            day['wind_avg'] = day_aux['velmedia']

            # Mayor racha de velocidad del viento (m/s)
            day['wind_max'] = day_aux['racha']

            last_days.append(day)

        # Se devuelven los datos
        return last_days

    def generate_year(self, y = 2017, min_attrb = 10):
        """
        Genera la información del año que recibe por parámetro
        """

        # Se obtienen los datos del año
        data = self.get_year(y)

        # Contendrá los datos de cada mes del año
        year = []

        # Se guarará la temperata máxima y el mes en el que se ha producido
        temp_max = dict()
        temp_max['temp'] = "-1000"
        temp_max['month'] = "-1"

        # Se guardará la temperata mínima y el mes en el que se ha producido
        temp_min = dict()
        temp_min['temp'] = "1000"
        temp_min['month'] = "-1"

        # Se guardarán los días del mes y el mes en el que ha habido el mayor
        # número de días con sol (%)
        sun_max = dict()
        sun_max['per'] = "-1"
        sun_max['month'] = "-1"

        # Se recorren todos los meses
        for i, month_aux in enumerate(data):

            # Se guardará la información relevante de cada mes
            month = dict()

            # Mes del que se obtiene la información
            month['month'] = i

            # Puede que el mes no esté completo si aún no ha terminado, por lo
            # que si no tiene datos, no se guarda nada
            if len(month_aux) > min_attrb:

                # Temperatura mínima del mes (ºC)
                month['temp_min'] = month_aux['ta_min']

                # Temperatura máxima del mes (ºC)
                month['temp_max'] = month_aux['ta_max']

                # Humedad relativa del mes (%)
                month['humidity'] = month_aux['hr']

                # Días de sol (%)
                month['sun'] = month_aux['p_sol']

                # Se añaden los datos al vector
                year.append(month)

                # Se comprueba la temperatura máxima para actualizarla
                if month['temp_max'] > temp_max['temp']:
                    temp_max['temp'] = month['temp_max']
                    temp_max['month'] = i

                # Se comprueba la temperatura mínima para actualizarla
                if month['temp_min'] < temp_min['temp']:
                    temp_min['temp'] = month['temp_min']
                    temp_min['month'] = i

                # Se comprueba el número de días máximo de sol para actualizarlos
                if month['sun'] > sun_max['per']:
                    sun_max['per'] = month['sun']
                    sun_max['month'] = i

        # Se guardan todos los datos que forman parte del año
        year = [year, [temp_max, temp_min, sun_max], y]

        return year

    def exec_query(self, query, reconn = True):
        """
        Ejecuta una petición a la Api con la consulta de los datos que se
        quieren obtener.
        Por defecto, ejecuta una segunda consulta para obtener los datos que
        se quieren.
        Devuelve el resultado de la petición
        """

        # Se hace la petición que se debe realizar
        self.conn.request("GET", f"/opendata"+query+"?api_key="+self.api_key, \
                            headers=self.headers)

        # Se guarda en "res" el resultado formateado en json con la respuesta
        # de la api
        res = json.loads(self.conn.getresponse().read() \
                            .decode('utf-8','ignore'))

        # Dependiendo de las peticiones que se hagan, puede que la respuesta
        # sea una url hacia donde hacer la petición que realmente obtiene los
        # datos que se piden. Si es ese caso, se realiza otra petición a la
        # ruta correcta
        if reconn:

            self.conn.request("GET", res['datos'], headers=self.headers)

            res = json.loads(self.conn.getresponse().read() \
                            .decode('utf-8','ignore'))

        # Se devuelve el json con la respuesta
        return res



    def to_string(self):
        """
        Devuelve el contenido de la Api como un string
        """

        res = self.weather

        return res

    #
    ########

#
################################################################################
