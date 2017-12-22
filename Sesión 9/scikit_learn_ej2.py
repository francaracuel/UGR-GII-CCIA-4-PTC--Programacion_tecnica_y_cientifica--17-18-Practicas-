# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:53:20 2017

@author: silve
"""

from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']

cad = []
cad2 = []

for t,marker, c in zip(range(3), ">ox", "rgb") :
    aux = plt.scatter(features[target == t, 0],
                features[target == t, 1],
                marker = marker,
                c=c,
                s=100)
    cad.append(aux)
    cad2.append(data.target_names[t])
plt.legend(cad, cad2, ncol=1, loc='upper right', )
plt.show()
