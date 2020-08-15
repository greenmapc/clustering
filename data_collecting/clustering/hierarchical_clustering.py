# Импортируем библиотеки
import inline as inline
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as shc

data = pd.read_csv('../transformed_data.csv', encoding='cp1251', sep=',')
data_scaled = data
data_scaled = pd.DataFrame(data_scaled, columns=data.columns)
data_scaled.head()


plt.figure(figsize=(10, 7))
plt.title("Dendrograms")
dend = shc.dendrogram(shc.linkage(data_scaled, method='ward'))
plt.show()
