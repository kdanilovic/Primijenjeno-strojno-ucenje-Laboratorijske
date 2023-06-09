# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 12:08:00 2018

@author: Grbic
"""

import scipy as sp
from sklearn import cluster, datasets
import numpy as np
import matplotlib.pyplot as plt

try:
    face = sp.face(gray=True)
except AttributeError:
    from scipy import misc
    face = misc.face(gray=True)
    

import matplotlib.image as mpimg
sl = mpimg.imread('example.png')

X = sl.reshape((-1,3)) # We need an (n_sample, n_feature) array
k_means = cluster.KMeans(n_clusters=3,n_init=1)
k_means.fit(X) 
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
face_compressed = np.choose(labels, values)
face_compressed.shape = sl.shape

plt.figure(1)
plt.imshow(sl,  cmap='gray')
plt.show()

plt.figure(2)
plt.imshow(face_compressed,  cmap='gray')
plt.show()