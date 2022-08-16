from sklearn import datasets
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