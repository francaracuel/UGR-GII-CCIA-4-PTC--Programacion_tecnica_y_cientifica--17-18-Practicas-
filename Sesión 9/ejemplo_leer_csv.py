import pandas as pd
from sklearn import svm
data = pd.read_csv(open('prueba.csv'))
print(data)
##target = data["dato1"]
target = data["clase"]
del data["clase"]

##print(data["dato1"])
##print(data["dato2"])
##print(target)

##clf = svm.SVC().fit(data, target)
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression().fit(data, target)

import numpy as np
cont = 0
y_pred = []
## for x1, x2 in [(5,21), (4,6), (7,3)] :
for x1, x2 in zip(data["dato1"], data["dato2"]) :
  X = np.array([x1,x2]).reshape(1,-1)
  y_pred.append(clf.predict(X))
  print(clf.predict(X), target[cont])
  cont += 1
##print(clf.predict([6,32]))
X = np.array([4,6]).reshape(1,-1)
print(clf.predict(X))
X = np.array([7,3]).reshape(1,-1)
print(clf.predict(X))

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
y_true = target
print(accuracy_score(y_true, y_pred))
print( accuracy_score(y_true, y_pred, normalize=False))
print(confusion_matrix(y_true, y_pred))


import numpy as np
data = np.array([(23, 12) ,(45, 3) ,(67, 4) ,(32,12) ,(76, 43) ,(12, 3)])
target = np.array([0,0,1,1,0,0,])
clf = svm.SVC().fit(data, target)
X= np.array([(23,12)])
print(clf.predict(X))
