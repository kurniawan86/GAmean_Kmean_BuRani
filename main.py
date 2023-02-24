#ini adalah program GA kmean, GAmean kmean
import random
import math
import pandas as pd
import numpy as np
import csv
import openpyxl
from kmeans import class_kmeans
from my_kmeans import myKmeans
from DatasetPublic import class_dataset
from GAfile import GA
from objectiveFile import step
from GA_Polygamy import GAPoly
from kmeans_ori import ClusteringKmeans
#
# def readDataExcel():
#     file = pd.read_excel(open('borneo.xlsx', 'rb'))
#     dframe = pd.DataFrame(file, columns=(['x', 'y']))
#     return np.array(dframe)

if __name__ == '__main__':
    # # dataset iris
    # dataset = class_dataset()
    # dataset.irisDataset()
    # baris,dim =dataset.X.shape
    # nCluster = 3

    # # dataset wine
    # dataset = class_dataset()
    # dataset.wineDataset()
    # baris, dim = dataset.X.shape
    # nCluster = 2

    # # dataset wine
    # dataset = class_dataset()
    # dataset.breast_cancerDataset()
    # baris, dim = dataset.X.shape
    # nCluster = 2

    # dataset diabetes
    # - irisDataset
    # - wineDataset
    # - breast_cancerDataset
    # - diabetesDataset
    # - artificialDataset
    # - artificialDataset3D
    # - dataset_MobilePhone
    # - riau

    dataset = class_dataset()
    # dataset.artificialDataset3D()
    dataset.dataset_riau()
    baris, dim = dataset.X.shape
    # nCluster = len(set(dataset.y))
    nCluster = 5
    print("n cluster: ", nCluster)
    print("Dataset : ", dataset.X)

    #GA
    nPop = 20
    Cr = 0.7
    maxloop = 100
    Mr = 0.1
    objektif = step()

    # print("tes 2 dimension ", arr_2d)

    # TESTING MY K-MEANS
    # objCluster = myKmeans(dataset.X, nCluster, bestGA)
    # objCluster.printout()
    #
    # print("===================")
    print("GA-MEAN")
    # obj = GA(nPop, nCluster, dim, maxloop, Cr, Mr, dataset.X, dataset.y, objektif)
    # bestGA = obj.bestInd
    # arr = np.array(bestGA)
    # arr_2d = np.reshape(arr, (nCluster, len(dataset.X[0])))
    # print(arr_2d)
    # print(type(arr_2d))
    # obj = ClusteringKmeans(dataset.X, nCluster, arr_2d)
    # obj.learning()
    # centrodss = obj.allcentroid
    # print(np.array(centrodss))
    # file = open('mydata.xlsx', 'w')
    # file = csv.writer(file)
    # file.writerow(['centroid ke-', 'latitute', 'longitute'])
    # for i in range (len(centrodss)):
    #     for j in range (nCluster):
    #         lat = centrodss[i][j][0]
    #         long = centrodss[i][j][1]
    #         file.writerow([j, lat, long])
    #     print()
    # print("===================")
    print("GA Poly Kmeans")

    print("===================")
    print("K-mean")
    # obj = GA(nPop, nCluster, dim, maxloop, Cr, Mr, dataset.X, dataset.y, objektif)
    # bestGA = obj.bestInd
    # arr = np.array(bestGA)
    # arr_2d = np.reshape(arr, (nCluster, len(dataset.X[0])))

    # print(dataset.X)
    arrdataset= np.array(dataset.X)
    centroid = []
    for i in range(nCluster):
        x = []
        for j in range (len(dataset.X[0])):
            mini = math.floor(min(arrdataset[:,j]))
            maxi = math.floor(max(arrdataset[:,j]))
            x.append(random.randint(mini, maxi))
        centroid.append(x)
    arrCent = np.array(centroid)
    print("centroid : ", arrCent)
    # print(type(arrCent))
    # obj = ClusteringKmeans(dataset.X, nCluster, centroid)
    # obj.learning()
    # centrodss = obj.allcentroid
    # print(np.array(centrodss))


    # file = open('mydata.xlsx', 'w')
    # file = csv.writer(file)
    # file.writerow(['centroid ke-', 'latitute', 'longitute'])
    # for i in range (len(centrodss)):
    #     for j in range (nCluster):
    #         lat = centrodss[i][j][0]
    #         long = centrodss[i][j][1]
    #         file.writerow([j, lat, long])
    #     print()
    print("===================")
    print("GA Poly Kmeans")
    # nmate = 4
    # obj1 = GAPoly(
    #     nmate,nPop, nCluster, dim, maxloop, Cr, Mr, dataset.X, dataset.y , objektif)
    # bestGApoly = obj1.bestInd
    # arr1 = np.array(bestGApoly)
    # arr_2d1 = np.reshape(arr1, (nCluster, len(dataset.X[0])))
    # obj = ClusteringKmeans(dataset.X, nCluster, arr_2d1)
    # obj.learning()
    # centrodss = obj.allcentroid
    # print(np.array(centrodss))
    # file = open('mydata.xlsx', 'w')
    # file = csv.writer(file)
    # file.writerow(['centroid ke-', 'latitute', 'longitute'])
    # for i in range (len(centrodss)):
    #     for j in range (nCluster):
    #         lat = centrodss[i][j][0]
    #         long = centrodss[i][j][1]
    #         file.writerow([j, lat, long])
    #     print()
    # print("===================")
    # print("GA Poly Kmeans")

    # print("===================")
    # print("K-mean")

    # obj = GA(nPop, nCluster, dim, maxloop, Cr, Mr, dataset.X, dataset.y, objektif)
    # bestGA = obj.bestInd
    # arr = np.array(bestGA)
    # arr_2d = np.reshape(arr, (nCluster, len(dataset.X[0])))
    # obj = ClusteringKmeans(dataset.X, nCluster, arr_2d)
    # obj.learning()

    # obj_kmeans = class_kmeans(dataset.X,dataset.y, nCluster, initCentroid=arr_2d)
    # obj_kmeans.get_SSE()
    # # obj_kmeans.get_silhouette()
    # # obj_kmeans.get_davies_bouldin()
    # # obj_kmeans.get_V_measure()
    # obj_kmeans.get_centroids()

    #
    # print("===================")
    # print("K- means")
    # initCentroids = []
    # obj_kmeans1 = class_kmeans(dataset.X,dataset.y, nCluster, initCentroid=initCentroids)
    # obj_kmeans1.get_SSE()
    # obj_kmeans1.get_silhouette()
    # obj_kmeans1.get_davies_bouldin()
    # obj_kmeans1.get_V_measure()
    # obj_kmeans1.get_centroids()
    #
    # print("===================")
    # print("GA Poly INIT")
    # nmate = 4
    # obj1 = GAPoly(
    #     nmate,nPop, nCluster, dim, maxloop, Cr, Mr, dataset.X, dataset.y , objektif)
    # bestGApoly = obj1.bestInd
    # arr1 = np.array(bestGApoly)
    # arr_2d1 = np.reshape(arr1, (nCluster, len(dataset.X[0])))
    # obj_kmeans2 = class_kmeans(dataset.X, dataset.y, nCluster, initCentroid=arr_2d1)
    # obj_kmeans2.get_SSE()
    # obj_kmeans2.get_silhouette()
    # obj_kmeans2.get_davies_bouldin()
    # obj_kmeans2.get_V_measure()
    # obj_kmeans2.get_centroids()
    # print("===================")
