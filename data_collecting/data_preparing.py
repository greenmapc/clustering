from sklearn import preprocessing
import pandas as pd
from scipy.sparse import csr_matrix
from scipy import sparse
from sklearn.preprocessing import StandardScaler
import numpy as np

#
# def color_transform(color):
#     result = []
#     for i in color:
#         result.append(int(i, 16))
#     return result
#
#
# lb = preprocessing.LabelBinarizer()
data_file = pd.read_csv('data.csv', encoding='cp1252', sep=',')
# data_file.head()
# brand_data = lb.fit_transform(list(set(data_file.brand.to_list())))
# print(lb.classes_)
# print(lb.transform(['Acura']))
# print(pd.DataFrame(brand_data))
# print(data_file)
# X=data_file.values[:,:]
# X= np.nan_to_num(X)
# print(X[0])
#
# color = color_transform(data_file.color)
# print(color)
#
# print(int(data_file.color[0], 16))
#
# # преобразовываем в векторы
# # Clus_dataSet=StandardScaler().fit_transform(X)
#
#
# def brand_transform(data_file):
#     return False
#


from sklearn.preprocessing import OneHotEncoder


def brand_transform(data_file):
    ohe = OneHotEncoder(sparse=False)
    new_ohe_features = ohe.fit_transform(data_file.brand.values.reshape(-1, 1))
    return pd.DataFrame(new_ohe_features, columns=['brand' + str(i) for i in range(new_ohe_features.shape[1])])


def model_transform(data_file):
    ohe = OneHotEncoder(sparse=False)
    new_ohe_features = ohe.fit_transform(data_file.model.values.reshape(-1, 1))
    return pd.DataFrame(new_ohe_features, columns=['model' + str(i) for i in range(new_ohe_features.shape[1])])


def body_type_transform(data_file):
    ohe = OneHotEncoder(sparse=False)
    new_ohe_features = ohe.fit_transform(data_file.body_type.values.reshape(-1, 1))
    return pd.DataFrame(new_ohe_features, columns=['body_type' + str(i) for i in range(new_ohe_features.shape[1])])


def write_transform_data_to_csv(data):
    data.to_csv('transformed_data.csv')


data = pd.concat([data_file, brand_transform(data_file), model_transform(data_file), body_type_transform(data_file)],
                 axis=1)
data = data.drop(['brand', 'model', 'body_type', 'color', 'region'], axis=1)
print(data)
