import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

import csv_generator
from clustering.plot_util import show_plot

data = pd.read_csv('../transformed_data.csv', encoding='cp1251', sep=',')
data_scaled = data
data_scaled = pd.DataFrame(data_scaled, columns=data.columns)
data_scaled.head()


def show_dendrogram(data_scaled):
    plt.figure(figsize=(10, 7))
    plt.title("Dendrograms")
    shc.dendrogram(shc.linkage(data_scaled, method='ward'))
    plt.show()


def clustering_result_to_csv(labels):
    simple_data = pd.read_csv('../data.csv', encoding='cp1251', sep=',')
    data = pd.concat([simple_data, pd.DataFrame(labels, columns=['cluster'])], axis=1)
    csv_generator.write_pd_to_csv(data, 'hierarchical_result.csv')

show_dendrogram(data_scaled)
cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
cluster.fit_predict(data_scaled)

clustering_result_to_csv(cluster.labels_)

labels = cluster.labels_

show_plot(data_scaled, 'price', 'year', labels)
show_plot(data_scaled, 'price', 'owners_count', labels)
show_plot(data_scaled, 'price', 'mileage', labels)
