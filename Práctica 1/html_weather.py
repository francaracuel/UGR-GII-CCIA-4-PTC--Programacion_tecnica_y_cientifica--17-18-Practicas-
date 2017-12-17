# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programación Técnica y Científica

4º - GII - CCIA - ETSIIT - UGR

Curso 2017/2018

Práctica 1 - Gestión de datos metereológicos proporcionados por la AEMET

Clase Html_Weather - Crea código HTML con los datos del clima

"""

from weather import *

################################################################################
# Clase Html_Weather
#
class Html_Weather:
    """
    Crea código HTML con los datos del clima
    """

    ########
    # Constructor
    #
    def __init__(self, weather, path, filename_output = "output.html", \
        days = 7, \
        year = 2017, \
        name = "Francisco Javier Caracuel Beltr&aacute;n", \
        title = "Pr&aacute;ctica 1", \
        subject = "Programaci&oacute;n T&eacute;cnica y Cient&iacute;fica", \
        c_year = "2017/2018"):
        """
        Guarda en la clase el objeto weather que contiene los datos del clima
        """

        # Guarda el objeto con los datos del clima
        self.weather = weather

        # Se guarda la ruta donde se debe alojar la página
        self.path = path

        # Se guarda el nombre del fichero html
        self.filename_output = filename_output

        # Variable donde se va guardando el contenido html
        self.html = ""

        # Se guardan los datos de la práctica
        self.name = name
        self.title = title
        self.subject = subject
        self.c_year = c_year

        # Se generan las gráficas
        self.gen_charts(days, year)

    #
    ########

    ########
    # Getters
    #



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

    def gen_charts(self, days = 7, year = 2017):
        """
        Genera las gráficas que se mostrarán en el fichero HTML
        """

        self.weather.create_chart_predictions_temperature("Temperatura en los próximos días", \
                            "Días", "Temperatura (ºC)", "Máximos", "Mínimos", show = False)

        self.weather.create_chart_predictions_rain("Probabilidad de lluvia en los próximos días", \
                            "Días", "Lluvia (%)", legend = False, show = False)

        self.weather.create_chart_predictions_wind("Viento en los próximos días", \
                            "Días", "Velocidad (m/s)", legend = False, show = False)

        self.weather.create_chart_year_sun("Porcentaje de días con sol ("+str(year)+")", \
                            "Mes", "Días de sol (%/mes)", legend = False, show = False)

        self.weather.create_chart_last_temperature("Temperaturas de los últimos "+str(days+1)+" días", \
                            "Días", "Temperatura (ºC)", legend = False, show = False, \
                            xlabel = "Días", ylabel = "Tipo de temperaturas", \
                            zlabel = "Temperatura (ºC)")

        self.weather.create_chart_compare_predictions_temperature("Comparación de temperatura real con la predicha", \
                            "Días", "Temperatura (ºC)", "Máximos", "Mínimos", show = False)

    def gen_all(self):
        """
        Genera todo el código HTML
        """

        self.gen_init()

        self.gen_head()

        self.gen_body()

        self.gen_end()

    def gen_init(self):
        """
        Crea la etiqueta principal del fichero html
        """

        self.html += """
        <!doctype html>
            <html xmlns="http://www.w3.org/1999/xhtml" lang="es" xml:lang="es">
        """

    def gen_end(self):
        """
        Crea la etiqueta final del fichero html
        """

        self.html += """
        </html>
        """

    def gen_head(self):
        """
        Crea las cabeceras del fichero html
        """

        #self.html += """<head>
        #                    <title>"""+ \
        #                        self.title+" - "+self.name+" - "+self.subject \
        #                    +"""</title>
        #                </head>"""

        self.html += """
            <head>
            	<meta charset="UTF-8">
            	<meta name="viewport" content="width=device-width, initial-scale=1">
                <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />

            	<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,300,700' rel='stylesheet' type='text/css'>

        """

        self.gen_css()

        self.gen_js()

        self.html += """
            	<script src="js/modernizr.js"></script> <!-- Modernizr -->

                <title>"""+ \
                    self.title+" - "+self.name+" - "+self.subject \
                +"""</title>

            </head>
        """

    def gen_body(self):
        """
        Crea el contenido principal del fichero html
        """

        # Se obtienen los datos para no hacer muchas llamadas al objeto weather
        predictions = self.weather.get_predictions()
        current = self.weather.get_current()
        last_days = self.weather.get_last_days()
        year = self.weather.get_year()
        months = self.weather.get_months()

        self.html += """
            <body>

                <div class="cd-pricing-container cd-has-margins">

            		<ul class="cd-pricing-list">

            			<li class="cd-popular" id="li_all">
            				<header class="cd-pricing-header">
            					<h2>"""+self.name+"""</h2>
                                <h2>"""+self.title+"""</h2>
                                <h2>"""+self.subject+"""</h2>
                                <h2>"""+self.c_year+"""</h2>
            				</header> <!-- .cd-pricing-header -->

            			</li>

            		</ul> <!-- .cd-pricing-list -->
            	</div> <!-- .cd-pricing-container -->

            	<header class="cd-header">
            		<h1>El tiempo en """+self.weather.get_city()+"""
                    : """+self.weather.get_date()+"""</h1>
            	</header>

            	<div class="cd-pricing-container cd-full-width cd-secondary-theme">
            		<ul class="cd-pricing-list">

                        <li class="cd-popular">
            				<header class="cd-pricing-header">
            					<h2>Tiempo actual</h2>

            					<div class="cd-price">
            						<span class="cd-currency">&#8451;</span>
            						<span class="cd-value">"""+\
                                    str(current['temp_current']) +\
                                    """</span>
            					</div>
            				</header> <!-- .cd-pricing-header -->

            				<div class="cd-pricing-body">
            					<ul class="cd-pricing-features">

            						<li>Precipitaci&oacute;n acumulada: <em>"""+\
                                    str(current['rain'])+""" mm</em></li>

            						<li>Velocidad m&aacute;xima del viento: <em>"""+\
                                    str(current['wind_max'])+""" m/s</em></li>

            						<li>Velocidad media del viento: <em>"""+\
                                    str(current['wind_avg'])+""" m/s</em></li>

            						<li>Direcci&oacute;n media del viento: <em>"""+\
                                    str(current['wind_dir'])+"""</em></li>

            						<li>Presi&oacute;n instant&aacute;nea: <em>"""+\
                                    str(current['pressure'])+""" hPa</em></li>

                                    <li>Humedad relativa en el aire: <em>"""+\
                                    str(current['humidity'])+""" %</em></li>

                                    <li>Temperatura en el suelo: <em>"""+\
                                    str(current['temp_floor'])+""" &#8451;</em></li>

                                    <li>Temperatura m&iacute;nima: <em>"""+\
                                    str(current['temp_min'])+""" &#8451;</em></li>

                                    <li>Temperatura m&aacute;xima: <em>"""+\
                                    str(current['temp_max'])+""" &#8451;</em></li>

                                    <li>Temperatura en el punto de roc&iacute;o: <em>"""+\
                                    str(current['temp_dew'])+""" &#8451;</em></li>

                                    <li>Visibilidad: <em>"""+\
                                    str(current['visibility'])+""" km</em></li>

            					</ul>
            				</div> <!-- .cd-pricing-body -->

            			</li>

            			<li>
            				<header class="cd-pricing-header">
            					<h2>A&ntilde;o</h2>

            					<div class="cd-price">
            						<span class="cd-value">"""+str(year[2])+"""</span>
            					</div>
            				</header> <!-- .cd-pricing-header -->

            				<div class="cd-pricing-body">
            					<ul class="cd-pricing-features">

            						<li>Temperatura m&aacute;xima: <em>"""+\
                                    str(year[1][0]['temp'])+""" &#8451;</em></li>

                                    <li>Mes: <em>"""+\
                                    str(months[year[1][0]['month']])+"""</em></li>

                                    <br/>

                                    <li>Temperatura m&iacute;nima: <em>"""+\
                                    str(year[1][1]['temp'])+""" &#8451;</em></li>

                                    <li>Mes: <em>"""+\
                                    str(months[year[1][1]['month']])+"""</em></li>

                                    <br/>

                                    <li>D&iacute;as de sol: <em>"""+\
                                    str(year[1][2]['per'])+""" %</em></li>

                                    <li>Mes: <em>"""+\
                                    str(months[year[1][2]['month']])+"""</em></li>

            					</ul>
            				</div> <!-- .cd-pricing-body -->
            			</li>

            		</ul> <!-- .cd-pricing-list -->

            	</div> <!-- .cd-pricing-container -->

            	<div class="cd-pricing-container cd-has-margins">

            		<ul class="cd-pricing-list">

            			<li class="cd-popular" id="li_all">
            				<header class="cd-pricing-header">
            					<h2>Gr&aacute;ficas</h2>
            				</header> <!-- .cd-pricing-header -->

            				<div class="cd-pricing-body">
            					<ul class="cd-pricing-features">
                                    <li><img src="compare_predictions_temperature.svg"/></li>
            						<li><img src="predictions_temperature.svg"/></li>
                                    <li><img src="predictions_rain.svg"/></li>
                                    <li><img src="predictions_wind.svg"/></li>
                                    <li><img src="last_temperature.svg"/></li>
                                    <li><img src="year_sun.svg"/></li>
            					</ul>
            				</div> <!-- .cd-pricing-body -->

            			</li>

            		</ul> <!-- .cd-pricing-list -->
            	</div> <!-- .cd-pricing-container -->
            </body>
        """

    def gen_css(self):
        """
        Crea el css del fichero HTML
        """

        self.html += """

        <style type="text/css">

            *, *::after, *::before {
              -webkit-box-sizing: border-box;
              -moz-box-sizing: border-box;
              box-sizing: border-box;
            }

            html {
              font-size: 62.5%;
            }

            html * {
              -webkit-font-smoothing: antialiased;
              -moz-osx-font-smoothing: grayscale;
            }

            body {
              font-size: 1.4rem;
              font-family: "Open Sans", sans-serif;
              color: #173d50;
              background-color: #50173d;
            }

            a {
              color: #50173d;
              text-decoration: none;
            }

            img{
                max-width: 100%;
            }

            /* --------------------------------

            Main Components

            -------------------------------- */
            .cd-header {
              height: 100px;
              line-height: 50px;
              position: relative;
            }
            .cd-header h1 {
              text-align: center;
              color: #FFFFFF;
              font-size: 1.5rem;
            }
            @media only screen and (min-width: 768px) {
              .cd-header {
                height: 160px;
                line-height: 100px;
              }
              .cd-header h1 {
                font-size: 3.6rem;
                font-weight: 300;
              }
            }

            .cd-pricing-container {
              width: 90%;
              max-width: 1170px;
              margin: 4em auto;
            }
            @media only screen and (min-width: 768px) {
              .cd-pricing-container {
                margin: 6em auto;
              }
              .cd-pricing-container.cd-full-width {
                width: 100%;
                max-width: none;
              }
            }

            .cd-pricing-list {
              margin: 2em 0 0;
              list-style: none;
            }

            #li_all{
                width: 100%;
            }

            .cd-pricing-list > li {
              margin-bottom: 1em;
              background-color: #FFFFFF;
              -webkit-backface-visibility: hidden;
              backface-visibility: hidden;
              /* Firefox bug - 3D CSS transform, jagged edges */
              outline: 1px solid transparent;
            }
            .cd-pricing-list > li::after {
              /* subtle gradient layer on the right - to indicate it's possible to scroll */
              content: '';
              position: absolute;
              top: 0;
              right: 0;
              height: 100%;
              width: 50px;
              pointer-events: none;
              background: -webkit-linear-gradient( right , #FFFFFF, rgba(255, 255, 255, 0));
              background: linear-gradient(to left, #FFFFFF, rgba(255, 255, 255, 0));
            }
            .cd-pricing-list > li.is-ended::after {
              /* class added in jQuery - remove the gradient layer when it's no longer possible to scroll */
              display: none;
            }
            @media only screen and (min-width: 768px) {
              .cd-pricing-list {
                margin: 3em 0 0;
              }
              .cd-pricing-list:after {
                content: "";
                display: table;
                clear: both;
              }
              .cd-pricing-list > li {
                width: 50%;
                float: left;
              }
              .cd-pricing-list > li::before {
                /* separator between pricing tables - visible when number of tables > 3 */
                content: '';
                position: absolute;
                z-index: 6;
                left: -1px;
                top: 50%;
                bottom: auto;
                -webkit-transform: translateY(-50%);
                -moz-transform: translateY(-50%);
                -ms-transform: translateY(-50%);
                -o-transform: translateY(-50%);
                transform: translateY(-50%);
                height: 50%;
                width: 1px;
                background-color: #b1d6e8;
              }
              .cd-pricing-list > li::after {
                /* hide gradient layer */
                display: none;
              }
              .cd-pricing-list > li.cd-popular {
                box-shadow: inset 0 0 0 3px #50173d;
              }
              .cd-pricing-list > li.cd-popular::before {
                /* hide table separator for .cd-popular table */
                display: none;
              }
              .cd-pricing-list > li.cd-popular + li::before {
                /* hide table separator for tables following .cd-popular table */
                display: none;
              }
              .cd-has-margins .cd-pricing-list > li, .cd-has-margins .cd-pricing-list > li.cd-popular {
                box-shadow: 0 1px 5px rgba(0, 0, 0, 0.1);
              }
              .cd-secondary-theme .cd-pricing-list > li {
                background: #3aa0d1;
                background: -webkit-linear-gradient( bottom , #3aa0d1, #3ad2d1);
                background: linear-gradient(to top, #3aa0d1, #3ad2d1);
              }
              .cd-secondary-theme .cd-pricing-list > li.cd-popular {
                background: #50173d;
                background: -webkit-linear-gradient( bottom , #e97d68, #e99b68);
                background: linear-gradient(to top, #e97d68, #e99b68);
                box-shadow: none;
              }
              .cd-pricing-list:nth-of-type(1)::before {
                /* hide table separator for the first table */
                display: none;
              }
              .cd-has-margins .cd-pricing-list > li {
                width: 32.3333333333%;
                float: left;
                margin-right: 1.5%;
                border-radius: 4px 4px 6px 6px;
              }
              .cd-has-margins .cd-pricing-list > li:last-of-type {
                margin-right: 0;
              }
              .cd-has-margins .cd-pricing-list > li::before {
                display: none;
              }
            }
            @media only screen and (min-width: 1500px) {
              .cd-full-width .cd-pricing-list > li {
                padding: 2.5em 0;
              }
            }

            @media only screen and (min-width: 768px) {
              .cd-popular .cd-pricing-wrapper > li::before {
                /* hide table separator for .cd-popular table */
                display: none;
              }
            }
            .cd-pricing-header {
              position: relative;
              z-index: 1;
              height: 80px;
              padding: 1em;
              pointer-events: none;
              background-color: #3aa0d1;
              color: #FFFFFF;
            }
            .cd-pricing-header h2 {
              margin-bottom: 3px;
              font-weight: 700;
              text-transform: uppercase;
            }
            .cd-popular .cd-pricing-header {
              background-color: #50173d;
            }
            @media only screen and (min-width: 768px) {
              .cd-pricing-header {
                height: auto;
                padding: 1.9em 0.9em 1.6em;
                pointer-events: auto;
                text-align: center;
                color: #173d50;
                background-color: transparent;
              }
              .cd-popular .cd-pricing-header {
                color: #50173d;
                background-color: transparent;
              }
              .cd-secondary-theme .cd-pricing-header {
                color: #FFFFFF;
              }
              .cd-pricing-header h2 {
                font-size: 1.8rem;
                letter-spacing: 2px;
              }
            }

            .cd-currency, .cd-value {
              font-size: 3rem;
              font-weight: 300;
            }

            .cd-duration {
              font-weight: 700;
              font-size: 1.3rem;
              color: #8dc8e4;
              text-transform: uppercase;
            }
            .cd-popular .cd-duration {
              color: #f3b6ab;
            }
            .cd-duration::before {
              content: '/';
              margin-right: 2px;
            }

            @media only screen and (min-width: 768px) {
              .cd-value {
                font-size: 7rem;
                font-weight: 300;
              }

              .cd-currency, .cd-duration {
                color: rgba(23, 61, 80, 0.4);
              }
              .cd-popular .cd-currency, .cd-popular .cd-duration {
                color: #50173d;
              }
              .cd-secondary-theme .cd-currency, .cd-secondary-theme .cd-duration {
                color: #2e80a7;
              }
              .cd-secondary-theme .cd-popular .cd-currency, .cd-secondary-theme .cd-popular .cd-duration {
                color: #ba6453;
              }

              .cd-currency {
                display: inline-block;
                margin-top: 10px;
                vertical-align: top;
                font-size: 2rem;
                font-weight: 700;
              }

              .cd-duration {
                font-size: 1.4rem;
              }
            }
            .cd-pricing-body {
              margin-bottom: 50px;
              overflow-x: auto;
              -webkit-overflow-scrolling: touch;
            }
            @media only screen and (min-width: 768px) {
              .cd-pricing-body {
                overflow-x: visible;
              }
            }

            .cd-pricing-features {
              width: 600px;
            }
            .cd-pricing-features:after {
              content: "";
              display: table;
              clear: both;
            }
            .cd-pricing-features li {
              width: 100px;
              float: left;
              padding: 1.6em 1em;
              font-size: 1.4rem;
              text-align: center;
              white-space: nowrap;
              overflow: hidden;
              text-overflow: ellipsis;
            }
            .cd-pricing-features em {
              display: block;
              margin-bottom: 5px;
              font-weight: 600;
            }
            @media only screen and (min-width: 768px) {
              .cd-pricing-features {
                width: auto;
              }
              .cd-pricing-features li {
                float: none;
                width: 95%;
                padding: 1em;
              }
              .cd-popular .cd-pricing-features li {
                margin: 0 3px;
              }
              .cd-pricing-features li:nth-of-type(2n+1) {
                background-color: rgba(23, 61, 80, 0.06);
              }
              .cd-pricing-features em {
                display: inline-block;
                margin-bottom: 0;
              }
              .cd-has-margins .cd-popular .cd-pricing-features li, .cd-secondary-theme .cd-popular .cd-pricing-features li {
                margin: 0;
              }
              .cd-secondary-theme .cd-pricing-features li {
                color: #FFFFFF;
              }
              .cd-secondary-theme .cd-pricing-features li:nth-of-type(2n+1) {
                background-color: transparent;
              }
            }

            .cd-pricing-footer {
              position: absolute;
              z-index: 1;
              top: 0;
              left: 0;
              /* on mobile it covers the .cd-pricing-header */
              height: 80px;
              width: 100%;
            }
            .cd-pricing-footer::after {
              /* right arrow visible on mobile */
              content: '';
              position: absolute;
              right: 1em;
              top: 50%;
              bottom: auto;
              -webkit-transform: translateY(-50%);
              -moz-transform: translateY(-50%);
              -ms-transform: translateY(-50%);
              -o-transform: translateY(-50%);
              transform: translateY(-50%);
              height: 20px;
              width: 20px;
              background: url(../img/cd-icon-small-arrow.svg);
            }
            @media only screen and (min-width: 768px) {
              .cd-pricing-footer {
                position: relative;
                height: auto;
                padding: 1.8em 0;
                text-align: center;
              }
              .cd-pricing-footer::after {
                /* hide arrow */
                display: none;
              }
              .cd-has-margins .cd-pricing-footer {
                padding-bottom: 0;
              }
            }

            .cd-select {
              position: relative;
              z-index: 1;
              display: block;
              height: 100%;
              /* hide button text on mobile */
              overflow: hidden;
              text-indent: 100%;
              white-space: nowrap;
              color: transparent;
            }
            @media only screen and (min-width: 768px) {
              .cd-select {
                position: static;
                display: inline-block;
                height: auto;
                padding: 1.3em 3em;
                color: #FFFFFF;
                border-radius: 2px;
                background-color: #0c1f28;
                font-size: 1.4rem;
                text-indent: 0;
                text-transform: uppercase;
                letter-spacing: 2px;
              }
              .no-touch .cd-select:hover {
                background-color: #112e3c;
              }
              .cd-popular .cd-select {
                background-color: #50173d;
              }
              .no-touch .cd-popular .cd-select:hover {
                background-color: #ec907e;
              }
              .cd-secondary-theme .cd-popular .cd-select {
                background-color: #0c1f28;
              }
              .no-touch .cd-secondary-theme .cd-popular .cd-select:hover {
                background-color: #112e3c;
              }
              .cd-has-margins .cd-select {
                display: block;
                padding: 1.7em 0;
                border-radius: 0 0 4px 4px;
              }
            }

        </style>
        """

    def gen_js(self):
        """
        Genera el contenido JavaScript
        """

        self.html += """

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

        <script>
            jQuery(document).ready(function($){
            	//hide the subtle gradient layer (.cd-pricing-list > li::after) when pricing table has been scrolled to the end (mobile version only)
            	checkScrolling($('.cd-pricing-body'));
            	$(window).on('resize', function(){
            		window.requestAnimationFrame(function(){checkScrolling($('.cd-pricing-body'))});
            	});
            	$('.cd-pricing-body').on('scroll', function(){
            		var selected = $(this);
            		window.requestAnimationFrame(function(){checkScrolling(selected)});
            	});

            	function checkScrolling(tables){
            		tables.each(function(){
            			var table= $(this),
            				totalTableWidth = parseInt(table.children('.cd-pricing-features').width()),
            		 		tableViewport = parseInt(table.width());
            		 	console.log(table.scrollLeft() - totalTableWidth + tableViewport)
            			if( table.scrollLeft() >= totalTableWidth - tableViewport - 1) {
            				table.parent('li').addClass('is-ended');
            			} else {
            				table.parent('li').removeClass('is-ended');
            			}
            		});
            	}
            });
        </script>

        """

    def export_html(self):
        """
        Guarda el contenido html (que se encuentra en la variable self.html) en
        un fichero en el lugar que se ha indicado
        """

        # Se abre el fichero con opciones de escritura
        f = open(self.path+self.filename_output, 'w')

        # Se añade el contenido
        f.write(self.html)

        # Se cierra el flujo abierto
        f.close()

    #
    ########

#
################################################################################
