# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:57:01 2016

@author: mgs
"""


import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
### from nolearn.dbn import DBN
import timeit
from sklearn.datasets import load_iris

## train = pd.read_csv("train.csv")
## features = train.columns[1:]
## X = train[features]
## y = train['label']

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']


X = features
y = target
X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.1,random_state=0)

clf_rf = RandomForestClassifier()
clf_rf.fit(X_train, y_train)
y_pred_rf = clf_rf.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred_rf)
print ("random forest accuracy: ",acc_rf)

clf_sgd = SGDClassifier()
clf_sgd.fit(X_train, y_train)
y_pred_sgd = clf_sgd.predict(X_test)
acc_sgd = accuracy_score(y_test, y_pred_sgd)
print ("stochastic gradient descent accuracy: ",acc_sgd)

clf_svm = LinearSVC()
clf_svm.fit(X_train, y_train)
y_pred_svm = clf_svm.predict(X_test)
acc_svm = accuracy_score(y_test, y_pred_svm)
print ("Linear SVM accuracy: ",acc_svm)

clf_svm = SVC()
clf_svm.fit(X_train, y_train)
y_pred_svm = clf_svm.predict(X_test)
acc_svm = accuracy_score(y_test, y_pred_svm)
print (" SVM accuracy: ",acc_svm)

clf_knn = KNeighborsClassifier()
clf_knn.fit(X_train, y_train)
y_pred_knn = clf_knn.predict(X_test)
acc_knn = accuracy_score(y_test, y_pred_knn)
print ("nearest neighbors accuracy: ",acc_knn)

### clf_nn = DBN([X_train.shape[1], 300, 10],learn_rates=0.3,learn_rate_decays=0.9,epochs=15)
### clf_nn.fit(X_train, y_train)
### acc_nn = clf_nn.score(X_test,y_test)
### print ("neural network accuracy: ",acc_nn)
