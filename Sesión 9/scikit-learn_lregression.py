# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:19:58 2016

@author: mgs
"""

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']

# Normalizacion
features -= np.mean(features, axis=0)
features /= np.std(features, axis=0)

#Etiquetado binario
is_versicolor = target == 1
binary_target = np.zeros(len(target))
binary_target[is_versicolor] = 1

# Validacion cruzada con 5 grupos
kf = KFold(n=len(binary_target), n_folds=5, shuffle=True)
cv= 0
for tr, tst in kf:
    #Train Test Split
    tr_features = features[tr, :]
    tr_target = binary_target[tr]
    tst_features = features[tst, :]
    tst_target = binary_target[tst]

    # Entrenamiento con Logistic Regression
    model = LogisticRegression()
    model.fit(tr_features, tr_target)

    # Medir exactitud del ajuste
    tr_accuracy = np.mean(model.predict(tr_features) == tr_target)
    tst_accuracy = np.mean(model.predict(tst_features) == tst_target)
    print ("%d Fold Train Accuracy: %f, Test accuracy: %f" % (cv, tr_accuracy, tst_accuracy))
    cv +=1
