import math

class step:
    def fitness(self, x):
        bar, kol = x.shape
        sod = 0
        for i in range(bar):
            for j in range(bar):
                dis = 0
                dis = dis + self.__calDistEuclid(x[i], x[j])
            #     print("dis", dis)
            # print("----")
            sod = sod + dis
        # print("sod :", sod)
        return sod

    def __calDistEuclid(self, x1, x2):
        # print("x1 :",x1)
        # print("x2 :",x2)
        n = len(x1)
        tot = 0
        for i in range (n):
            # euclid
            tot = tot + (math.pow((x1[i] - x2[i]),2))
        return math.sqrt(tot)
