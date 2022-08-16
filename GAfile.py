import random
import numpy as np
import numpy.random as rnd
import math

from matplotlib import pyplot as plt

class gen:
    __ndim = None
    __bound = None
    position = []
    fitness = 0
    
    def __init__(self, nDim, bound=None):
        self.__ndim = nDim
        self.__bound = bound
        self.__initPosition()

    def __initPositionNoBound(self):
        gen = []
        for i in range(self.__ndim):
            gen.append(random.random())
        return gen

    def __initPositionBound(self):
        gen = []
        mini = self.__bound[0]
        maxi = self.__bound[1]
        for i in range(self.__ndim):
            ind = random.randint(mini, maxi-1)
            gen.append(ind)
        return gen

    def __initPosition(self):
        if self.__bound == None:
            self.position = self.__initPositionNoBound()
        else:
            self.position = self.__initPositionBound()

    def viewPosition(self):
        print(self.position)

class GA:
    nPop = None
    pop = None
    nDim = 0
    bound = None
    function = None
    bestInd = None
    bestFitness = 0
    loop = 0
    nElit = 0
    newpop = []
    fitness = []

    def __init__(self, nPop, ncluster, dim, max_itarasi,Cr,Mr,Function=None, bound=None):
        self.loop = max_itarasi
        self.nPop = nPop
        self.nDim = ncluster*dim
        self.bound = bound
        self.function = Function
        self.mainAlgorithm(Cr, Mr)

    def initPosition(self):
        swarm = []
        for i in range(self.nPop):
            swarm.append(gen(self.nDim, bound=self.bound))
        self.pop = swarm

    def viewPosition(self):
        for i in range(self.nPop):
            print("no :", i, ": ",self.pop[i].position)
    
    def calFitness(self):
        for i in range(self.nPop):
            fit = (self.function.fitness(
                self.pop[i].position))
            self.pop[i].fitness = fit
    
    def viewFitness(self):
        for i in range(self.nPop):
            print("fitness : ", self.pop[i].fitness)
            
    def getGbest(self):
        i = self.__findGbestMin()
        self.bestInd = self.pop[i].position
        self.bestFitness = self.pop[i].fitness
    
    def __findGbestMin(self):
        mini = self.pop[0].fitness
        index = 0
        for i in range(self.nPop):
            if mini > self.pop[i].fitness:
                index = i
                mini = self.pop[i].fitness
        return index

    def __selec_turnamen(self):
        selec = np.random.randint(self.nPop)
        for xi in np.random.randint(0,self.nPop,3):
            if self.pop[xi].fitness < self.pop[selec].fitness:
                selec = xi
        return self.pop[selec].position

    def pickParent(self):
        selected = [self.__selec_turnamen() for _ in range(self.nPop)]
        return selected

    def crossover(self, p1, p2, Cr):
        offspring = []
        offspring1 , offspring2 = p1.copy(), p2.copy()
        if rnd.rand() < Cr:
            c1 = rnd.rand()
            c2 = 1 - c1
            offspringA = list(np.array(offspring1)*c1)
            offspringB = list(np.array(offspring2)*c2)
            offspringC = list(np.array(offspring1)*c2)
            offspringD = list(np.array(offspring2)*c1)
            self.add_newPop(offspringA+offspringB)
            self.add_newPop(offspringC)
        else:
            self.add_newPop(offspring1)
            self.add_newPop(offspring2)

    def kawin_polygamy(self):
        pass

    def mutation(self,Mr):
        mut = math.floor(self.nPop * Mr)
        for i in range(mut):
            child = []
            for j in range(self.nDim):
                child.append(rnd.rand())
            self.add_newPop(child)

    def elitisme(self):
        n = self.nPop
        if n % 2 == 0:
            self.add_newPop(self.bestInd)
            self.add_newPop(self.bestInd)
            self.nElit = 2
        else:
            self.add_newPop(self.bestInd)
            self.nElit = 1

    def add_newPop(self, pop):
        self.newpop.append(pop)

    def replacePop(self):
        for i in range(self.nPop):
            self.pop[i].position = self.newpop[i]
        self.newpop = []

    def mainAlgorithm(self, cr,mr):
        self.initPosition()
        self.viewPosition()
        error = []
        for i in range(self.loop):
            self.calFitness()   #calculate Fitness
            self.getGbest()     #find Gbest
            self.elitisme()     #elitisme
            #crossover
            for i in range(
                    self.nElit,self.nPop-math.floor(mr*self.nPop),2):
                selected = self.pickParent()
                self.crossover(selected[i],selected[i+1],cr)
            self.mutation(mr)   #mutation
            self.replacePop()   #replace oldPop with newPop
            error.append(self.bestFitness)
            self.fitness.append(self.bestFitness)
        plt.plot(error)
        plt.show()
            # print("best individu =",self.bestInd)