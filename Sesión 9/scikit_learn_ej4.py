# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:58:56 2017

@author: silve
"""

from sklearn.model_selection import train_test_split
from sklearn import datasets
iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target


Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris,random_state=1)

# PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2, svd_solver='randomized', whiten=True)
pca = pca.fit(Xtrain)

Xtrain_pca = pca.transform(Xtrain)
Xtest_pca = pca.transform(Xtest)

from sklearn.naive_bayes import GaussianNB # 1. escoger modelo
model = GaussianNB()                  # 2. instanciar modelo
model.fit(Xtrain_pca, ytrain)                  # 3. ajustar modelo a datos
y_model = model.predict(Xtest_pca)    # 4. predecir nuevos datos
from sklearn.metrics import accuracy_score
print(accuracy_score(ytest, y_model))
