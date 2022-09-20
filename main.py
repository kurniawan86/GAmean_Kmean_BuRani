#ini adalah program GA kmean, GAmean kmean
import pandas as pd
import numpy as np
from kmeans import class_kmeans
from my_kmeans import myKmeans
from DatasetPublic import class_dataset
from GAfile import GA
from objectiveFile import step
#
# def readDataExcel():
#     file = pd.read_excel(open('borneo.xlsx', 'rb'))
#     dframe = pd.DataFrame(file, columns=(['x', 'y']))
#     return np.array(dframe)

if __name__ == '__main__':
    # data = readDataExcel()
    dataset = class_dataset()
    dataset.irisDataset()
    baris,dim =dataset.X.shape
    # print("dimdim :",dim)
    nCluster = 3

    #GA
    nPop = 20
    Cr = 0.7
    maxloop = 100
    Mr = 0.1
    objektif = step()
    obj = GA(nPop, nCluster,  dim, maxloop, Cr, Mr, dataset.X, dataset.y, objektif)
    # print(obj.fitness)
    bestGA = obj.bestInd
    # print("len dim ",len(dataset.X[0]))

    arr = np.array(bestGA)
    # print("ARRR :",arr)
    arr_2d = np.reshape(arr,(nCluster, len(dataset.X[0])))
    # print("tes 2 dimension ", arr_2d)


    # TESTING MY K-MEANS
    # objCluster = myKmeans(dataset.X, nCluster, bestGA)
    # objCluster.printout()

    # initCentroids = np.array([[1,1],[0,0]])
    print("===================")
    obj_kmeans = class_kmeans(dataset.X,dataset.y, nCluster, initCentroid=arr_2d)
    obj_kmeans.get_SSE()
    obj_kmeans.get_silhouette()
    obj_kmeans.get_davies_bouldin()
    obj_kmeans.get_V_measure()

    print("===================")
    initCentroids = []
    obj_kmeans1 = class_kmeans(dataset.X,dataset.y, nCluster, initCentroid=initCentroids)
    obj_kmeans1.get_SSE()
    obj_kmeans1.get_silhouette()
    obj_kmeans1.get_davies_bouldin()
    obj_kmeans1.get_V_measure()

    #random with range
    # print(np.random.uniform(low=-6.5, high=13.3, size=(2, 3)))
    # asu = np.array([[2, 5, 4],
    #    [3, 3, 4],[3,3,3]])
    # ob = step()
    # ob.fitness(asu)