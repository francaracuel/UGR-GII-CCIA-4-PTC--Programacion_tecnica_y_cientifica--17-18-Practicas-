# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programación Técnica y Científica

4º - GII - CCIA - ETSIIT - UGR

Curso 2017/2018

Práctica 2 - Gestión de test - Corrector del test

Clase Gui - Contiene la interfaz gráfica para corregir los tests

"""

# Se importan las clases necesarias para trabajar con los datos
from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import *
from xml_corrector import *
import sys

################################################################################
# Clase Gui
#
class Gui:
    """
    Gestiona la interfaz gráfica para corregir los tests
    """

    ########
    # Constructor
    #
    def __init__(self, title = "Práctica 2 - Realización de tests"):
        """
        Inicializa todos los elementos necesarios para que se pueda visualizar
        y rellenar correctamente el test
        """

        # Se crea el objeto que va a guardar las preguntas y respuestas en xml
        self.xml = Xml()

        # Se guarda el título de la ventana principal
        self.title = title

        # Se da nombre a las etiquetas del programa
        self.create_labels()

        # Tamaño de la ventana principal
        self.window_width = "300"
        self.window_height = "200"

        # Se inicializan las variables necesarias para la creación de la
        # interfaz
        self.initialize()

        # Se lanza la ventana para seleccionar el fichero a rellenar
        #self.load()

        # Se inicia el escuchador de eventos
        self.main()

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

    def create_labels(self):
        """
        Da nombre a las etiquetas que se van a utilizar para crear el test
        """

        self.label_button_correct = "Corregir los tests"

        self.label_menu_load_test = "Cargar plantilla"
        self.label_menu_load_tests = "Cargar tests para corregir"
        self.label_menu_exit = "Salir"
        self.label_menu_file = "Archivo"
        self.label_menu_about = "Acerca de"

        self.label_name = "Francisco Javier Caracuel Beltrán"
        self.label_practice = "Práctica 2 - Gestión de tests"
        self.label_subject = "Programación Técnica y Científica"
        self.label_year = "Curso 2017/2018"

        self.label_dialog_info_test_load_title = "Plantilla cargada"
        self.label_dialog_info_test_load_message = "La plantilla se ha cargado"

        self.label_dialog_info_tests_load_title = "Tests cargados"
        self.label_dialog_info_tests_load_message = "Los tests para corregir se han cargado"

        self.label_dialog_info_not_load_title = "Fichero no cargado"
        self.label_dialog_info_not_load_message = "El fichero no se ha podido cargar"

        self.label_dialog_info_not_load_title = "Fichero no cargado"
        self.label_dialog_info_not_load_message = "El fichero no se ha podido cargar"

        self.label_dialog_error_empty_filename_title = "Error"
        self.label_dialog_error_empty_filename_message = "No has indicado el nombre del fichero"

        self.label_dialog_error_load_xml_title = "Error leyendo fichero XML"
        self.label_dialog_error_load_xml_message = "El fichero seleccionado no es correcto"

        self.label_dialog_info_tests_corrected_title = "Tests corregidos"
        self.label_dialog_info_tests_corrected_message = "Se han corregido los tests correctamente"

        self.label_dialog_info_save_title = "Ficheros guardados"
        self.label_dialog_info_save_message = "Los ficheros se han guardado correctamente"

        self.label_dialog_info_not_save_title = "Ficheros no guardados"
        self.label_dialog_info_not_save_message = "Los ficheros no se han podido guardar"

        self.label_dialog_error_save_title = "Error al guardar los ficheros"
        self.label_dialog_error_save_message = "No se puede guardar si no hay preguntas válidas"

    def initialize(self):
        """
        Inicializa los elementos necesarios para que se pueda crear la
        estructura con los widgets
        """

        # Para añadir los widgets de manera ordenada, se tiene un contador
        # con el número de filas y columnas donde se van colocando
        self.row = 0
        self.col = 0

        # Variables utilizadas para mostrar el botón de corregir
        self.bool_load_test = False
        self.bool_load_tests = False

    def main(self):
        """
        Crea la estructura de los elementos visuales y lanza el escuchador de
        eventos
        """

        self.create_structure()

        # Inicia el escuchador de eventos
        self.root.mainloop()

    def create_structure(self):
        """
        Crea la estructura con las preguntas y respuestas
        """

        # Se inicia la ventana principal
        self.root = Tk()

        # Se añade el título de la ventana principal
        self.root.title(self.title)

        # Se impide que se pueda redimensionar la ventana
        self.root.resizable(0,0)

        # Se añade el tamaño de la ventana
        self.root.geometry(str(self.window_width)+"x"+str(self.window_height))

        # Se añade el menú
        self.create_menu()

        # Se crea un canvas para añadir un Frame con un ScrollBar, donde
        # finalmente se colocarán todos los widgets
        self.canvas = Canvas(self.root)
        self.canvas.pack(expand = True, side=LEFT, fill='both')

        # Se crea el scrollBar
        scrollbar = Scrollbar(self.root, command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill='y')

        # Se asigna el scroll al canvas
        self.canvas.configure(yscrollcommand = scrollbar.set)

        # Se indica que cuando ocurra cualquier evento se ajuste el scroll a
        # la ventana
        self.canvas.bind('<Configure>', self.on_configure)

        # Ha habido problemas para mostrar los últimos elementos que se
        # añaden, por lo que se añade un evento a la ventana en el que
        # cuando se detecta un movimiento del ratón, se ajusta
        self.root.bind('<Enter>', self.on_configure)
        self.root.bind('<Leave>', self.on_configure)

        # Se centra la ventana
        self.center(self.root)

        # Se añade la ventana principal
        #self.root.grid()

        # Se crea el Frame donde se colocan todos los widgets
        self.frame = Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.frame, anchor='nw')

        # Se aumenta la columna en 1
        self.row += 1

    def create_menu(self):
        """
        Añade el menú que va a tener el programa
        """

        # Se añade un menú prinicpal
        menubar = Menu(self.root)

        # Se crea un submenú par la gestión del xml
        filemenu1 = Menu(menubar)

        # Se crea la opción para cargar el test con la puntuación
        filemenu1.add_command(label = self.label_menu_load_test, \
                                                    command = self.load_test)

        # Se crea la opción para cargar los tests con las respuestas
        filemenu1.add_command(label = self.label_menu_load_tests, \
                                                    command = self.load_tests)

        # Se añade un separador
        filemenu1.add_separator()

        # Se crea la opción de salir
        filemenu1.add_command(label = self.label_menu_exit, command = self.exit)

        # Se añade el submenú al menú principal
        menubar.add_cascade(label = self.label_menu_file, menu = filemenu1)

        # Se añade un segundo submenú
        filemenu2 = Menu(menubar)

        # Se añade el nombre
        filemenu2.add_command(label = self.label_name)

        # Se añade el nombre de la práctica
        filemenu2.add_command(label = self.label_practice)

        # Se añade el nombre de la asignatura
        filemenu2.add_command(label = self.label_subject)

        # Se añade el año
        filemenu2.add_command(label = self.label_year)

        # Se añade el submenú al menú principal
        menubar.add_cascade(label = self.label_menu_about, menu = filemenu2)

        # Se indica a la ventana el menú que va a tener
        self.root.config(menu = menubar)

    def create_button_correct(self):
        """
        Añade un botón para guardar los datos
        """

        if self.bool_load_test and self.bool_load_tests:

            self.col = 0

            # Se añade la entrada de texto para escribir la pregunta
            button = Button(self.frame, text = self.label_button_correct, \
                                            command = self.correct)

            button.grid(row = self.row, column = self.col, sticky = W+E, \
                                                        padx = 10, pady = 10)

            self.row += 1
            self.col = 0


    def on_configure(self, event = None):
        """
        Actualiza el tamaño del scroll al contenido del frame
        """

        self.row += 1
        self.col = 0

        self.canvas.configure(scrollregion = self.canvas.bbox('all'))

    def load_test(self):
        """
        En base a un fichero xml, carga las preguntas que existen en él para
        editarlas
        """

        # Se establece a None por si mantiene el nombre del fichero de
        # operaciones anteriores
        self.filename = None

        # Se obtiene el nombre del xml donde se encuentran las preguntas y
        # respuestas
        self.dialog_load_file()

        # Si se ha seleccionado un fichero se continua, si no se muestra
        # un mensaje de error
        if self.filename:

            # Se indica el nombre del fichero para cargar los datos
            self.xml.set_filename_test(self.filename)

            try:

                # Se cargan los datos
                self.xml.load_test()

                self.bool_load_test = True

                self.create_button_correct()

                # Se muestra error al leer el fichero XML
                showinfo(title=self.label_dialog_info_test_load_title, \
                        message=self.label_dialog_info_test_load_message)

            except AttributeError:

                # Se muestra error al leer el fichero XML
                showerror(title=self.label_dialog_error_load_xml_title, \
                        message=self.label_dialog_error_load_xml_message)

        else:

            showerror(title=self.label_dialog_error_empty_filename_title, \
                    message=self.label_dialog_error_empty_filename_message)

    def load_tests(self):
        """
        En base a un fichero xml, carga las preguntas que existen en él para
        editarlas
        """

        # Se establece a None por si mantiene el nombre del fichero de
        # operaciones anteriores
        self.filenames = None

        # Se obtiene el nombre del xml donde se encuentran las preguntas y
        # respuestas
        self.dialog_load_files()

        # Si se ha seleccionado un fichero se continua, si no se muestra
        # un mensaje de error
        if len(self.filenames) > 0:

            # Se indica el nombre del fichero para cargar los datos
            self.xml.set_filename_tests(self.filenames)

            try:

                # Se cargan los datos
                self.xml.load_tests()

                self.bool_load_tests = True

                self.create_button_correct()

                # Se muestra error al leer el fichero XML
                showinfo(title=self.label_dialog_info_tests_load_title, \
                        message=self.label_dialog_info_tests_load_message)

            except AttributeError:

                # Se muestra error al leer el fichero XML
                showerror(title=self.label_dialog_error_load_xml_title, \
                        message=self.label_dialog_error_load_xml_message)

        else:

            showerror(title=self.label_dialog_error_empty_filename_title, \
                    message=self.label_dialog_error_empty_filename_message)

    def exit(self):
        """
        Termina el programa
        """

        sys.exit()

    def dialog_load_file(self):
        """
        Abre una ventana para seleccionar donde se encuentra el fichero que
        contiene las preguntas y respuestas
        """

        self.filename = askopenfilename(defaultextension=".xml", \
                                        filetypes=[("Archivos XML","*.xml")])

        #print(self.filename)

    def dialog_load_files(self):
        """
        Abre una ventana para seleccionar donde se encuentra el fichero que
        contiene las preguntas y respuestas
        """

        self.filenames = askopenfilenames(defaultextension=".xml", \
                                        filetypes=[("Archivos XML","*.xml")])

        #print(self.filename)

    def dialog_save_file(self):
        """
        Abre una ventana para seleccionar el nombre y el lugar donde se debe
        guardar el fichero xml
        """

        self.filename = asksaveasfilename(defaultextension=".xml", \
                                        filetypes=[("Archivos XML","*.xml")])

    def center(self, toplevel):
        """
        Centra en pantalla el elemento que recibe.
        Referencia: https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter
        """

        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def correct(self):
        """
        Corrige los tests con la plantilla cargada
        """

        self.xml.correct()

        showinfo(title=self.label_dialog_info_tests_corrected_title, \
                message=self.label_dialog_info_tests_corrected_message)

        # Se establece a None por si mantiene el nombre del fichero de
        # operaciones anteriores
        self.filename = None

        # Se muestra una ventana para seleccionar el lugar donde se debe
        # guardar el test
        self.dialog_save_file()

        # Si se ha seleccionado un fichero se continua, si no se muestra
        # un mensaje de error
        if self.filename:

            # Se indica el nombre del fichero que debe crear
            self.xml.set_filename_result(self.filename)

            # Se guardan los datos en el fichero
            error = self.xml.save()

            # Se muestra un mensaje tanto si ha habido error como si no
            if not error:

                # Se muestra un mensaje informando de que se ha guardado
                showinfo(title=self.label_dialog_info_save_title, \
                                message=self.label_dialog_info_save_message)

            else:

                # Se muestra un mensaje informando de que no se ha guardado
                showinfo(title=self.label_dialog_info_not_save_title, \
                            message=self.label_dialog_info_not_save_message)

        else:

            showerror(title=self.label_dialog_error_empty_filename_title, \
                    message=self.label_dialog_error_empty_filename_message)

    #
    ########

#
################################################################################
