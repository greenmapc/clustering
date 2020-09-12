from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np


def standardization_data(data):
    X = data.values[:, 1:]
    X = np.nan_to_num(X)
    return StandardScaler().fit_transform(X)


def k_mean_clustering(data):
    clasterNum = 4
    k_maens = KMeans(init="k-means++", n_clusters=clasterNum, n_init=12)
    stnd_data = standardization_data(data)
    print(stnd_data)
    k_maens.fit(data)
    labels = k_maens.labels_
    print(labels)


import pandas as pd

data_file = pd.read_csv('../transformed_data.csv')
data_file.head()
print(data_file)
k_mean_clustering(data_file)
