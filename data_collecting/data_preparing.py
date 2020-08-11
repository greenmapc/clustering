import pandas as pd

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


data_file = pd.read_csv('data.csv', encoding='cp1252', sep=',')
data = pd.concat([data_file, brand_transform(data_file), model_transform(data_file), body_type_transform(data_file)],
                 axis=1)
data = data.drop(['brand', 'model', 'body_type', 'color', 'region'], axis=1)
