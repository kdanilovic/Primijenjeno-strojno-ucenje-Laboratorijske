import numpy as np
from sklearn.datasets import fetch_openml
import joblib
import pickle
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier



X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)


# TODO: prikazi nekoliko ulaznih slika
fig = plt.figure
#img1 = X[0,:]
#img2 = X[1,:]
#img1 = img1.reshape((28,28))
#img2= img2.reshape((28,28))
#plt.imshow(img1, cmap='gray')
#plt.imshow(img2, cmap= 'gray')
#plt.show()
     


# skaliraj podatke, train/test split
X = X / 255.
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:] 


# TODO: izgradite vlastitu mrezu pomocu sckitlearn MPLClassifier 
mlp_mnist = MLPClassifier(random_state=1, max_iter=300).fit(X_train, y_train)
mlp_mnist.predict_proba(X_test[:1])
mlp_mnist.predict(X_test[:5,:])


print(mlp_mnist.score(X_test, y_test))




# TODO: evaluirajte izgradenu mrezu


# spremi mrezu na disk
filename = "NN_model.sav"
joblib.dump(mlp_mnist, filename)

