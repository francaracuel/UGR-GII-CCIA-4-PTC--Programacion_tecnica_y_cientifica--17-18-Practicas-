# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programación Técnica y Científica

4º - GII - CCIA - ETSIIT - UGR

Curso 2017/2018

Práctica 2 - Gestión de test - Creación del test

Clase Gui - Contiene la interfaz gráfica para crear los tests

"""

# Se importan las clases necesarias para trabajar con los datos
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
from xml_creator import *
import sys

################################################################################
# Clase Gui
#
class Gui:
    """
    Gestiona la interfaz gráfica para crear los tests
    """

    ########
    # Constructor
    #
    def __init__(self, title = "Práctica 2 - Creación de tests"):
        """
        Inicializa todos los elementos necesarios para que se pueda visualizar
        y crear correctamente el test
        """

        # Se crea el objeto que va a guardar las preguntas y respuestas en xml
        self.xml = Xml()

        # Se guarda el título de la ventana principal
        self.title = title

        # Se da nombre a las etiquetas del programa
        self.create_labels()

        # Tamaño de la ventana principal
        self.window_width = "620"
        self.window_height = "400"

        # Se inicializan las variables necesarias para la creación de la
        # interfaz
        self.initialize()

        # Se inicia el escuchador de eventos
        self.main()

    #
    ########

    ########
    # Getters
    #

    def get_data(self):
        """
        Obtiene los datos que se han introducido en la interfaz gráfica ya
        guardados en su estructura correctamente
        """

        # Guarda los datos
        self.save()

        return self.data

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

        self.label_question = "Pregunta"
        self.label_answer = "Respuesta"

        self.label_button_question = "Añade otra pregunta"
        self.label_button_answer = "Añade otra respuesta"

        self.label_score = "Puntuación"
        self.label_per = "Porcentaje"
        self.label_per2 = "%"

        self.label_button_save = "Guardar cuestionario"

        self.label_menu_load = "Cargar"
        self.label_menu_save = "Guardar"
        self.label_menu_exit = "Salir"
        self.label_menu_file = "Archivo"
        self.label_menu_about = "Acerca de"

        self.label_name = "Francisco Javier Caracuel Beltrán"
        self.label_practice = "Práctica 2 - Gestión de tests"
        self.label_subject = "Programación Técnica y Científica"
        self.label_year = "Curso 2017/2018"

        self.label_dialog_error_save_title = "Error al guardar los ficheros"
        self.label_dialog_error_save_message = "No se puede guardar si no hay preguntas válidas"

        self.label_dialog_info_save_title = "Ficheros guardados"
        self.label_dialog_info_save_message = "Los ficheros se han guardado correctamente"

        self.label_dialog_info_not_save_title = "Ficheros no guardados"
        self.label_dialog_info_not_save_message = "Los ficheros no se han podido guardar"

        self.label_dialog_info_not_load_title = "Fichero no cargado"
        self.label_dialog_info_not_load_message = "El fichero no se ha podido cargar"

        self.label_dialog_error_empty_filename_title = "Error"
        self.label_dialog_error_empty_filename_message = "No has indicado el nombre del fichero"

        self.label_dialog_yes_no_title = "¡Atención!"
        self.label_dialog_yes_no_message = "Todos los datos se perderán. ¿Deseas continuar?"

        self.label_dialog_error_load_xml_title = "Error leyendo fichero XML"
        self.label_dialog_error_load_xml_message = "El fichero seleccionado no es correcto"

    def initialize(self):
        """
        Inicializa los elementos necesarios para que se pueda crear la
        estructura con los widgets
        """

        # Para añadir los widgets de manera ordenada, se tiene un contador
        # con el número de filas y columnas donde se van colocando
        self.row = 0
        self.col = 0

        # Se cuenta el número de preguntas que va realizando (-1 al sumar 1
        # al crear la pregunta y empezar el índice de la lista en 0)
        self.num_questions = -1

        # Se cuenta el número de respuestas de cada pregunta
        self.num_answers = 1

        # Se establece el mínimo y máximo valor que se puede asignar a las
        # preguntas
        self.question_value_min = 0
        self.question_value_max = 10
        self.question_value_increment = 1

        # Se establece el mínimo y máximo valor que se puede asignar a las
        # respuestas
        self.answer_value_min = -150
        self.answer_value_max = 100
        self.answer_value_increment = 10

        # Color del separador
        self.color_separator = "gray"

        # Estructura de datos para guardar los elementos que forman parte de
        # la interfaz gráfica
        self.questions = []
        self.answers = []

    def main(self):
        """
        Crea la estructura de los elementos visuales y lanza el escuchador de
        eventos
        """

        self.create_structure()

        # Inicia el escuchador de eventos
        self.root.mainloop()

    def create_structure(self, with_data = False):
        """
        Crea la estructura con las preguntas y respuestas
        """

        # Si se va a cargar los datos del xml, la estructura principal no es
        # necesaria
        if not with_data:

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

        # Añade el botón para guardar el cuestionario
        self.create_button_save()

        # Añade el botón para insertar más preguntas
        self.create_button_question()

        # Añade el botón para insertar más respuestas
        self.create_button_answer()

        # Se aumenta la columna en 1
        self.row += 1

        # Si se empieza desde 0, se añade una pregunta
        if not with_data:

            # Se añade una pregunta
            self.create_question()

    def create_menu(self):
        """
        Añade el menú que va a tener el programa
        """

        # Se añade un menú prinicpal
        menubar = Menu(self.root)

        # Se crea un submenú par la gestión del xml
        filemenu1 = Menu(menubar)

        # Se crea la opción para cargar un fichero xml para editarlo
        filemenu1.add_command(label = self.label_menu_load, command = self.load)

        # Se crea la opción de guardar el test
        filemenu1.add_command(label = self.label_menu_save, command = self.save)

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

    def create_question(self, text = "", score = 1, with_data = False):
        """
        Añade una pregunta a la ventana
        """

        # Se añade un separador para diferenciar entre preguntas
        self.create_separator()

        # Se aumenta el contador de preguntas
        self.num_questions += 1

        # Se inicializa el número de respuestas de la pregunta
        self.num_answers = 1

        # Pregunta
        label = Label(self.frame, text = self.label_question+" "+ \
                                                str(self.num_questions+1)+":")

        # Se añade a la ventana
        label.grid(row = self.row, column = self.col, sticky = W, padx = 10, \
                                                                   pady = 10)

        self.col += 1

        # Se le da un valor por defecto a la pregunta (vacío si no se indica
        # nada en el argumento)
        var = StringVar(self.root, text)

        # Se añade la entrada de texto para escribir la pregunta
        entry_box = Entry(self.frame, width = 50, textvariable = var)

        entry_box.grid(row = self.row, column = self.col, columnspan = 2, \
                                        sticky = W+E, padx = 10, pady = 10)

        self.col += 2

        # Puntuación
        label = Label(self.frame, text = self.label_score+":")

        # Se añade a la ventana
        label.grid(row = self.row, column = self.col, sticky = W, padx = 10, \
                                                                    pady = 10)

        self.col += 1

        # Se le da un valor por defecto al selector de puntuación, que será 0
        var = StringVar(self.root, str(score))

        # Se añade el selector de puntuación
        spin_box = Spinbox(self.frame, from_ = self.question_value_min, \
                                    to = self.question_value_max, \
                                    increment = self.question_value_increment,
                                    textvariable = var,
                                    width = 5)

        spin_box.grid(row = self.row, column = self.col)

        # Se añade el texto a las preguntas para recuperarlo al final
        self.questions.append([entry_box, spin_box])

        # Se añade el botón para añadir más respuestas
        #self.create_button_answer()

        self.row += 1
        self.col = 0

        if not with_data:

            self.create_answer()
            self.create_answer()

        #self.create_separator()

    def create_answer(self, text = "", per = 0):
        """
        Añade al Frame una nueva respuesta
        """

        # Respuesta
        label = Label(self.frame, text = self.label_answer+" "+ \
                                                    str(self.num_answers)+":")

        # Se añade a la ventana
        label.grid(row = self.row, column = self.col, sticky = W, padx = 10, \
                                                                    pady = 10)

        self.col += 1

        # Se le da un valor por defecto a la respuesta (vacío si no se indica
        # nada en el argumento)
        var = StringVar(self.root, text)

        # Se añade la entrada de texto para escribir la pregunta
        entry_box = Entry(self.frame, textvariable = var)

        entry_box.grid(row = self.row, column = self.col, columnspan = 2, \
                                            sticky = W+E, padx = 10, pady = 10)

        self.col += 2

        # Puntuación
        label = Label(self.frame, text = self.label_per+":")

        # Se añade a la ventana
        label.grid(row = self.row, column = self.col, sticky = W, padx = 10, \
                                                                    pady = 10)

        self.col += 1

        # Se le da un valor por defecto al selector de puntuación, que será 0
        var = StringVar(self.root, str(per))

        # Se añade el selector de puntuación
        spin_box = Spinbox(self.frame, from_ = self.answer_value_min, \
                                    to = self.answer_value_max, \
                                    increment = self.answer_value_increment,
                                    textvariable = var,
                                    width = 5)

        spin_box.grid(row = self.row, column = self.col)

        self.col += 1

        # %
        label = Label(self.frame, text = self.label_per2)

        # Se añade a la ventana
        label.grid(row = self.row, column = self.col, sticky = W, padx = 10, \
                                                                    pady = 10)

        # Se añade el elemento que contiene la respuesta y su valor al
        # contenedor para recuperar la información cuando se quiera.
        # Si es la primera respuesta se crea un nuevo subcontenedor
        if self.num_answers == 1:
            self.answers.append([(entry_box, spin_box)])
        # Si no es la primera respuesta, se concantena a las que ya hay
        else:
            self.answers[self.num_questions].append((entry_box, spin_box))

        self.row += 1
        self.col = 0

        self.num_answers += 1

        self.on_configure()

    def create_separator(self):
        """
        Añade un Frame con poca altura de manera que parece un separador
        """

        separator = Frame(self.frame)
        separator.grid(row = self.row, column = self.col, columnspan = 6, \
                                                                sticky = W+E)

        separator.config(bg=self.color_separator)

        self.row += 1
        self.col = 0

    def create_button_save(self):
        """
        Añade un botón para guardar los datos
        """

        self.col = 1

        # Se añade la entrada de texto para escribir la pregunta
        button = Button(self.frame, text = self.label_button_save, \
                                        command = self.save)

        button.grid(row = self.row, column = self.col, sticky = W+E, \
                                                        padx = 10, pady = 10,
                                                        columnspan = 3)

        self.row += 1
        self.col = 0

    def create_button_question(self):
        """
        Añade un botón que permite añadir una nueva pregunta
        """

        self.col = 0

        # Se añade la entrada de texto para escribir la pregunta
        button = Button(self.frame, text = self.label_button_question, \
                                        command = self.create_question)

        button.grid(row = self.row, column = self.col, sticky = W+E, \
                                                        padx = 30, pady = 10,
                                                        columnspan = 3)

        #self.row += 1
        self.col = 0

    def create_button_answer(self):
        """
        Añade un botón que permite añadir una nueva respuesta a la última
        pregunta que se haya creado
        """

        self.col = 3

        # Se añade la entrada de texto para escribir la pregunta
        button = Button(self.frame, text = self.label_button_answer, \
                                        command = self.create_answer)

        button.grid(row = self.row, column = self.col, sticky = W+E, \
                                                        padx = 30, pady = 10,
                                                        columnspan = 3)

        #self.row += 1
        self.col = 0

    def on_configure(self, event = None):
        """
        Actualiza el tamaño del scroll al contenido del frame
        """

        self.row += 1
        self.col = 0

        self.canvas.configure(scrollregion = self.canvas.bbox('all'))

    def load(self):
        """
        En base a un fichero xml, carga las preguntas que existen en él para
        editarlas
        """

        # Como se va a sustituir toda la ventana, se pregunta si se quiere
        # hacer
        res = askyesno(self.label_dialog_yes_no_title, \
                                            self.label_dialog_yes_no_message)

        # Si se desea cargar todo, se elimina el contenido en el Frame
        if res:

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
                self.xml.set_filename(self.filename)

                try:

                    # Se cargan los datos
                    self.xml.load()

                    # Se obtienen los datos
                    self.data = self.xml.get_data()

                    # Se comprueba si se tienen datos cargados
                    if len(self.data) > 0:

                        # Se eliminan todos los widgets
                        self.frame.destroy()

                        # Se inicializan las variables necesarias
                        self.initialize()

                        # Se añaden todas las preguntas y respuestas a la
                        # ventana
                        self.create_structure(with_data = True)

                        # Se recorre la estructura de datos
                        for question in self.data:

                            # Se añade la pregunta
                            self.create_question(question[0], question[1], \
                                                            with_data = True)

                            # Se recorren las respuestas de la pregunta
                            for answer in question[2]:

                                # Se añade la respuesta
                                self.create_answer(answer[0], answer[1])

                        # Se ajusta el scroll
                        self.on_configure()



                    else:

                        # Se muestra un mensaje informando de que no se ha
                        # cargado
                        showinfo(title=self.label_dialog_info_not_load_title, \
                                message=self.label_dialog_info_not_load_message)

                except AttributeError:

                    # Se muestra error al leer el fichero XML
                    showerror(title=self.label_dialog_error_load_xml_title, \
                            message=self.label_dialog_error_load_xml_message)

            else:

                showerror(title=self.label_dialog_error_empty_filename_title, \
                        message=self.label_dialog_error_empty_filename_message)

    def save(self):
        """
        Recorre todos los widgets con las entradas de datos y los convierte
        a una estructura de pregunta y respuestas con sus puntuaciones de
        manera que es comprensible para la clase Xml.
        Si una pregunta tiene su contenido vacío se ignora. Si una respuesta
        tiene su contenido vacío, se ignora.
        """

        self.data = []

        # Se recorren todas las preguntas
        for i, question in enumerate(self.questions):

            # Si una pregunta está vacío, no se añade
            if question[0].get():

                answers = []

                # Por cada pregunta se recorren sus respuestas
                for answer in self.answers[i]:

                    # Si una respuesta no está vacía, no se añade
                    if answer[0].get():
                        answers.append((answer[0].get(), answer[1].get()))

                # Solo se añadirá una pregunta si tiene un mínimo de dos
                # respuestas
                if len(answers) >= 2:

                    # En cada tupla se añade la pregunta y su valor y una lista con
                    # todas las respuestas correspondientes y su porcentaje
                    self.data.append((question[0].get(), question[1].get(), answers))

        #print(self.data)

        # Si hay alguna pregunta se guarda el fichero
        if len(self.data) > 0:

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
                self.xml.set_filename(self.filename)

                # Se envía la estructura de datos con las preguntas y respuestas
                self.xml.set_data(self.data)

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

        # Si no hay ninguna pregunta se muestra un mensaje de error
        else:
            showerror(title=self.label_dialog_error_save_title, \
                                message=self.label_dialog_error_save_message)

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

    def dialog_save_file(self):
        """
        Abre una ventana para seleccionar el nombre y el lugar donde se debe
        guardar el fichero xml
        """

        self.filename = asksaveasfilename(defaultextension=".xml", \
                                        filetypes=[("Archivos XML","*.xml")])

        #print(self.filename)

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

    #
    ########

#
################################################################################
