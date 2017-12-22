# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 00:19:50 2017

@author: silve
"""

import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets
iris = datasets.load_iris()
features = iris.data
target = iris.target

features -= np.mean(features, axis=0)
features /= np.std(features, axis=0)
#División en entrenamiento (tr) y test (tst)
kf = KFold(n_splits=2, random_state=None, shuffle=False)
# En kf tendríamos las n_folds divisiones
for tr, tst in kf.split(features):
# for tr, tst in kf:
  tr_features = features[tr, :]
  tr_target = target[tr]
  tst_features = features[tst, :]
  tst_target = target[tst]
  #Ajuste
  model = LogisticRegression()
  model.fit(tr_features, tr_target)
  #Exactitud del ajuste
  tr_accuracy = np.mean(model.predict(tr_features) == tr_target)
  tst_accuracy = np.mean(model.predict(tst_features) == tst_target)
  print(tr_accuracy, tst_accuracy)
