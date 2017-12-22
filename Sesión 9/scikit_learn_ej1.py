# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:50:25 2017

@author: silve
"""

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(42)
x = 10 * rng.rand(50)
y = 2.5 * x - 2 + rng.randn(50)
plt.scatter(x, y);
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
X = x[:, np.newaxis]
X.shape
(50, 1)
model.fit(X, y)
print(model.coef_)
print(model.intercept_)

# Predicción de datos
xfit = np.linspace(-1, 11)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)
plt.scatter(x, y)
plt.plot(xfit, yfit);
