import math

class step:
    def fitness(self, x):
        sumof = 0
        for i in range(len(x)):
            sumof = sumof + math.pow((x[i] + 0.5), 2)
        return sumof