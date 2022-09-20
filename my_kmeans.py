import math

class myKmeans:
    data = []
    nCluster = 0
    centroid = []
    jarak = []
    index = []
    error = 0

    def __init__(self, data, ncluster, centroid):
        self.data = data
        self.nCluster = ncluster
        self.centroid = centroid
        self.Algoritma()

    def printout(self):
        print("centroid ", self.centroid)

    def Algoritma(self):
        errorLama = -1
        errorBaru = 0

        while errorLama != errorBaru:
            errorLama = errorBaru
        self.getAllJarak()

    def getAllJarak(self):
        n = len(self.data)
        dist = []
        for i in range(n):
            dist.append(self.getJarakSatuDataToCentroids(i))
        self.jarak=dist

    def jarak(self,data1,data2):
        print("def jarak: print data1", data1)
        print("def jarak: print data2", data2)
        n = len(data1)
        total=0
        for i in range(0,n):
            total = total + math.pow(data1[i]-data2[i],2)
        return math.sqrt(total)

    def getJarakSatuDataToCentroids(self,index):
        n = self.nCluster
        print("def getjaraksatudata:centroid:", self.centroid)
        print("def getjaraksatudata:data:", self.data[index])
        dist = []
        for i in range(n):
            jarak = self.jarak(self.data[index],self.centroid[i])
            dist.append(jarak)
        return dist

