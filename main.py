#ini adalah program GA kmean, GAmean kmean
import pandas as pd
import numpy as np
from kmeans import class_kmeans
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
    nCluster = 3

    #GA
    nPop = 10
    Cr = 0.8
    maxloop = 5
    Mr = 0.2
    objektif = step()
    obj = GA(nPop, nCluster,dim, maxloop, Cr, Mr, objektif)
    print(obj.fitness)
    print("best :",obj.bestInd)

    # initCentroids = np.array([[1,1],[0,0]])
    initCentroids = []
    obj_kmeans = class_kmeans(dataset.X,dataset.y, nCluster, initCentroid=initCentroids)
    obj_kmeans.get_SSE()
    obj_kmeans.get_silhouette()
    obj_kmeans.get_davies_bouldin()
    obj_kmeans.get_V_measure()


