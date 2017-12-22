# -*- coding: utf-8 -*-
"""

Francisco Javier Caracuel Beltrán

PTC - Programacion Técnica y Científica

4º - GII - CCIA - ETSIIT

Curso 2017/2018

Sesión 9

"""

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC

import pandas as pd

################################################################################
# Ejecuciones
#

if __name__ == '__main__':

    # Se cargan los datos del cáncer de mama
    #data = load_breast_cancer()

    #print(data['data'])

    # Se crean dos listas con las características y su etiqueta
    #x = data.data
    #y = data.target

    # Se separa las muestras en entrenamiento y test de manera aleatoria
    #x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

    # Se elige el modelo que se va a utilizar para hacer la predicción y se
    # instancia
    #model = GaussianNB()

    # Se ajusta el modelo a los datos
    #model.fit(x_train, y_train)

    # Se predice el resultado de los datos
    #y_model = model.predict(x_test)

    # Se muestra el porcentaje de acierto de las etiquetas generadas con las
    # reales que deberia tener
    #print(accuracy_score(y_test, y_model))





    file = open("bank.csv","r")

    data_csv = pd.read_csv(open('bank.csv'), sep=";")

    # Se cambian las etiquetas por valores numéricos
    data = pd.get_dummies(data_csv, columns =['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome', 'y'])

    # Se separan todos los datos en muestras y etiquetas
    x = data.iloc[:,1:]
    y = data.iloc[:,0]

    # Se crean las muestras de test y entrenamiento y sus correspondientes
    # etiquetas de test y entrenamiento
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

    clf_svm = LinearSVC()
    clf_svm.fit(x_train, y_train)
    y_pred_svm = clf_svm.predict(x_test)
    acc_svm = accuracy_score(y_test, y_pred_svm)
    print ("Linear SVM accuracy: ",acc_svm)

#
################################################################################
