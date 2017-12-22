# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:32:35 2016

@author: mgs
"""

N_FOLDS = 5

## http://scikit-learn.org/stable/modules/grid_search.html
def estimacion(model, tr_features, tr_target) :
    import numpy as np
    from sklearn.grid_search import GridSearchCV
    param_grid = [
       {'C': [1.0, 10.0, 100.0, 1000.0, 10000.0, 100000.0], 'kernel': ['linear']},
       {'C': [1.0, 10.0, 100.0, 1000.0, 10000.0, 100000.0], 'gamma': [0.001, 0.0001, 'auto'], 'kernel': ['rbf']} ]
    grid = GridSearchCV(estimator=model, param_grid= param_grid)
    grid.fit(tr_features, tr_target)
    return grid.best_estimator_.gamma, grid.best_estimator_.kernel, grid.best_estimator_.C


# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
from sklearn.svm import SVC
from sklearn.model_selection import KFold
## from matplotlib import pyplot as plt
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

# Validacion cruzada con N_FOLDS grupos
tr_media = 0
tst_media = 0

kf = KFold(n=len(binary_target), n_folds=N_FOLDS, shuffle=True)
cv= 0
for tr, tst in kf:
    #Train Test Split
    tr_features = features[tr, :]
    tr_target = binary_target[tr]
    tst_features = features[tst, :]
    tst_target = binary_target[tst]

    # Entrenamiento con SVM
    model = SVC()
    estimacion_svc = estimacion(model, tr_features, tr_target)
    print(estimacion_svc)
    model = SVC(gamma=estimacion_svc[0], kernel=estimacion_svc[1], C=estimacion_svc[2])
    ## model = SVC()
    model.fit(tr_features, tr_target)

    # Medir exactitud del ajuste, model.predict
    tr_accuracy = np.mean(model.predict(tr_features) == tr_target)
    tst_accuracy = np.mean(model.predict(tst_features) == tst_target)
    print ("%d Fold Train Accuracy: %f, Test accuracy: %f" % (cv, tr_accuracy, tst_accuracy))

    tr_media+=tr_accuracy
    tst_media+= tst_accuracy

    if cv==2 :
        model2= model
    cv +=1

print ("Media training: ", tr_media/N_FOLDS)
print ("Media test: ", tst_media/N_FOLDS)

tr_accuracy = np.mean(model2.predict(tr_features) == tr_target)
tst_accuracy = np.mean(model2.predict(tst_features) == tst_target)
print ("%d Fold Train Accuracy: %f, Test accuracy: %f" % (2, tr_accuracy, tst_accuracy))
