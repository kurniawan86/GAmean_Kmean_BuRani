from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics.cluster import v_measure_score
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score

class class_kmeans:
    X = []
    y = []
    init_centroids = []
    nCluster = 0
    y_pred = []
    centroids = []
    SSE = []

    def __init__(self, X,y, ncluster, initCentroid =None):
        self.X = X
        self.y = y
        self.nCluster = ncluster
        self.init_centroids = initCentroid
        self.clustering()

    def clustering(self):
        # print(len(self.init_centroids))
        if len(self.init_centroids) == 0:
            kmeans = KMeans(n_clusters=self.nCluster).fit(self.X)
        else:
            kmeans = KMeans(n_clusters=self.nCluster, init=self.init_centroids).fit(self.X)
        self.y_pred = kmeans.labels_
        self.centroids = kmeans.cluster_centers_
        # print(kmeans.score(self.data))
        self.SSE = kmeans.inertia_

    def get_V_measure(self):
        acc = v_measure_score(self.y, self.y_pred)
        print("V Measure score  :",acc)
        return acc

    def get_SSE(self):
        print("nilai SSE        : ",self.SSE)
        return self.SSE

    def get_silhouette(self):
        z = silhouette_score(self.X, self.y_pred)
        print("Silhoutte Score  :",z)
        return z

    def get_davies_bouldin(self):
        z = davies_bouldin_score(self.X, self.y_pred)
        print("Davies Boundies  :",z)
        return z

