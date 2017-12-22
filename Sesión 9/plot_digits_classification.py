"""
================================
Recognizing hand-written digits
================================

An example showing how the scikit-learn can be used to recognize images of
hand-written digits.

This example is commented in the
:ref:`tutorial section of the user manual <introduction>`.

"""
print(__doc__)

# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause

# Standard scientific Python imports
import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

# The digits dataset
digits = datasets.load_digits()

# The data that we are interested in is made of 8x8 images of digits, let's
# have a look at the first 4 images, stored in the `images` attribute of the
# dataset.  If we were working from image files, we could load them using
# matplotlib.pyplot.imread.  Note that each image must have the same size. For these
# images, we know which digit they represent: it is given in the 'target' of
# the dataset.
images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)

# We learn the digits on the first half of the digits
classifier.fit(data[:int(n_samples / 2)], digits.target[:int(n_samples / 2)])

# Now predict the value of the digit on the second half:
expected = digits.target[int(n_samples / 2):]
predicted = classifier.predict(data[int(n_samples / 2):])

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

images_and_predictions = list(zip(digits.images[int(n_samples / 2):], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()

from scipy.ndimage import imread
from scipy.ndimage import zoom

imagen = imread("digito_6_reducido2.jpg", flatten=False, mode=None)
plt.imshow(imagen, cmap="gray")
plt.show()
plt.figure()

import numpy as np
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
imagen = rgb2gray(imagen)

from skimage import filters
th = filters.threshold_otsu(imagen)
imagen2 = imagen<(th*0.85)
plt.imshow(imagen2, cmap="gray")
plt.show()
plt.draw()
plt.figure()

print(digits.images[0].shape)
plt.imshow(digits.images[0], cmap="gray")
plt.show()
plt.figure()

print(imagen2.shape)
print(digits.images[0].shape[0]*1.0/imagen2.shape[0], digits.images[0].shape[1]*1.0/imagen2.shape[1])
print(digits.images[0].shape[0], digits.images[0].shape[1])

imagen2 = zoom(imagen2, zoom=(digits.images[0].shape[0]*8.0/imagen2.shape[0], digits.images[0].shape[1]*8.0/imagen2.shape[1]), order=1)
print(imagen2.shape)
plt.matshow(imagen2, cmap="gray")
plt.show()

imagen2 = zoom(imagen2, zoom=(digits.images[0].shape[0]*1.0/imagen2.shape[0], digits.images[0].shape[1]*1.0/imagen2.shape[1]), order=1)
print(imagen2.shape)
plt.matshow(imagen2, cmap="gray")
plt.show()
print(classifier.predict(imagen2.flatten()))
