import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from scripts.polynomial_features import polynomial_features
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def one_hot_encode(df, column_name):
    dummies = pd.get_dummies(df[column_name], prefix=column_name)
    df = pd.concat([df, dummies], axis=1)
    df = df.drop(column_name, axis=1)
    return df
def process_data(df):
    df = one_hot_encode(df, 'Influencer')
    df = df.fillna(df.mean())
    return df

def get_features(df):
    X = df.drop('Sales', axis=1)
    y = df['Sales']
    return X, y

def data_split(X, y, test_size=0.33):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=0)
    return X_train, X_test, y_train, y_test

def  feature_scaling(X_train, x_test):
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(x_test)
    return X_train, X_test

def prepare_data(file_path, test_size=0.33):
    df = load_data(file_path)
    df = process_data(df)
    X, y = get_features(df)
    X_train, X_test, y_train, y_test = data_split(X, y, test_size=test_size)
    X_train, X_test = feature_scaling(X_train, X_test)
    X_train = polynomial_features(np.array(X_train))
    X_test = polynomial_features(np.array(X_test))
    y_train = np.array(y_train)
    y_test = np.array(y_test)
    return X_train, X_test, y_train, y_test


