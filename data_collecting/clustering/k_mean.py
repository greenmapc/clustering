import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

import csv_generator
from clustering.plot_util import show_plot


def standardization_data(data):
    X = data.values[:, 1:]
    return np.nan_to_num(X)


def k_mean_clustering(data):
    clasterNum = 3
    k_means = KMeans(init="k-means++", n_clusters=clasterNum, n_init=12)
    stnd_data = standardization_data(data)
    k_means.fit(stnd_data)
    return k_means.labels_


data_file = pd.read_csv('../transformed_data.csv', encoding='cp1251', sep=',')
data_file.head()
labels = k_mean_clustering(data_file)

show_plot(data_file, 'price', 'year', labels)
show_plot(data_file, 'price', 'owners_count', labels)
show_plot(data_file, 'price', 'mileage', labels)
simple_data = pd.read_csv('../data.csv', encoding='cp1251', sep=',')
data = pd.concat([simple_data, pd.DataFrame(labels, columns=['cluster'])], axis=1)
csv_generator.write_pd_to_csv(data, 'k_mean_result.csv')
