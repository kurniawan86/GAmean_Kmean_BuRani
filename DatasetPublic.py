from sklearn import datasets
import pandas as pd
import numpy as np
from numpy import genfromtxt

class class_dataset:
    X = []
    y = []

    def __init__(self):
        None

    def irisDataset(self):
        iris = datasets.load_iris()
        print("Dataset Iris FLowers")
        self.X = iris.data  # we only take the first two features.
        self.y = iris.target

    def wineDataset(self):
        wine = datasets.load_wine()
        print("Dataset Wine")
        self.X = wine.data  # we only take the first two features.
        self.y = wine.target
        # print("wine target", wine.target, len(self.y))

    def breast_cancerDataset(self):
        cancer = datasets.load_breast_cancer()
        print("Dataset Breast Cancer ")
        self.X = cancer.data
        self.y = cancer.target

    def diabetesDataset(self):
        df = genfromtxt('diabetes_dataset.csv',delimiter=',',skip_header=1)
        # print(df.shape)
        self.X = df[:,0:8]
        y = df[:,8:9]
        yy = []
        for i in range (len(y)):
            # print(y[i][0])
            yy.append(y[i][0])
        self.y = yy
        # print(yy)
        # print(np.array(yy))
        # self.X = list(X)
        # # X = X.tolist()
        # print(type(self.X))