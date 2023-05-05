from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage


def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

#1 zad

data = generate_data(500,1)
print(data)
plt.figure()
plt.scatter(data[:,0],data[:,1])

kmeans = KMeans(n_clusters=3, random_state=0, n_init="auto").fit(data)
print('Centers')
y_kmeans = kmeans.predict(data)

plt.scatter(data[:, 0], data[:, 1], c=y_kmeans, s=50, cmap='viridis')
print(kmeans.cluster_centers_)
centers = kmeans.cluster_centers_


plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);



#2 zad
list = []
for i in range(1,20):
    kmeans = KMeans(n_clusters=i, random_state=0, n_init="auto").fit(data)
    list.append(kmeans.inertia_)


plt.figure(2)
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],list)
plt.xlabel('Broj klastera')
plt.ylabel('Vrijednost inercije')




#3 zad

z=linkage(data,'ward')
fig=plt.figure()
dn=dendrogram(z)
plt.show()