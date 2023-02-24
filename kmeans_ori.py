import math
import random as rand

class ClusteringKmeans():
    error = []
    sse = []
    data = []
    nCluster = 0
    initCentroid = []
    centroids = []
    jarak = []
    index = []
    allcentroid = []

    def __init__(self, dataset, ncluster, initCent):
        self.initCentroid = initCent
        self.__initAttribute(dataset, ncluster)
        print("centroids awal : ",self.centroids)

    def __initAttribute(self,dataset, ncluster):
        self.centroids = self.initCentroid
        self.nCluster = ncluster
        self.data = dataset


    def initCentroid(self):
        cent = []
        for i in range(self.nCluster):
            x=[]
            for j in range(len(self.data[0])):
                [min,max]=self.getMinMax(self.data, j)
                print(min, max)
                x.append(rand.randint(min, max))
            cent.append(x)
        self.centroids = cent
        print("testing testing centroid : ",cent)

    def getMinMax(self, data, fiturke):
        n=len(data)
        min = data[0][fiturke]
        max = data[0][fiturke]
        for i in range (n):
            if min > data[i][fiturke]:
                min = data[i][fiturke]
            if max < data[i][fiturke]:
                max = data[i][fiturke]
        return min, max

    def learning(self):
        errorLama=-1
        errorBaru=0

        while errorLama != errorBaru:
            errorLama = errorBaru
            self.__gelAllJarak()
            self.__getAnggota()
            self.__getSumOfDistance()
            self.getCentroid()
            print("centroid by iterative : ",self.centroids)
            errorBaru = self.sse
            self.error.append(errorBaru)
            print("SSE :", self.error)
            self.allcentroid.append(self.centroids)

    def getCentroid(self):
        n = len(self.jarak)
        for i in range(self.nCluster):
            ang = []
            for j in range(n):
                if self.index[j] == i:
                    ang.append(self.data[j])
            if ang!=[]:
                self.centroids[i] = self.__mean(ang)
            else:
                self.centroids[i] = self.__getValueCentroid(i)
                # self.centroids[i] = 0

    def __getValueCentroid(self, index):
        # print("testing centroid : ", self.centroids[index])
        dis = self.__jarak(self.centroids[index], self.data[0])
        ind = 0
        for i in range(len(self.data)):
            distemp = self.__jarak(self.centroids[index], self.data[i])
            if dis > distemp:
                dis = distemp
                ind = i
        return self.data[ind]

    def __mean(self, data):
        n = len(data)
        m = len(data[0])
        tot = [0]*m
        for i in range(n):
            for j in range(m):
                tot[j] = tot[j]+data[i][j]
        for i in range(m):
            tot[i] = tot[i]/n
        return tot

    def __getSumOfDistance(self):
        n = len(self.jarak)
        error = 0
        for i in range(n):
            error = error+self.jarak[i][self.index[i]]
        self.sse = error

    def __gelAllJarak(self):
        n = len(self.data)
        dist = []
        for i in range(n):
            dist.append(self.getJarakSatuDataToCentroids(i))
        self.jarak = dist

    def getJarakSatuDataToCentroids(self, index):
        n = self.nCluster
        dist = []
        for i in range(n):
            jarak = self.__jarak(self.data[index], self.centroids[i])
            dist.append(jarak)
        return dist

    def __jarak(self, data1, data2):
        n = len(data1)
        total = 0
        for i in range(0, n):
            total = total+math.pow(data1[i]-data2[i], 2)
        return math.sqrt(total)

    def __getAnggota(self):
        n = len(self.data)
        x = self.jarak
        ind = []
        for i in range(n):
            ind.append(self.__getIndexMin(x[i]))
        self.index = ind

    def __getIndexMin(self, data):
        n = len(data)
        index = 0
        minimal = data[0]
        for i in range(1, n):
            if minimal > data[i]:
                index = i
                minimal = data[i]
        return index