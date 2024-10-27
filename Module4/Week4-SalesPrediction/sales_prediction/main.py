import numpy as np
from utils.metrics import r2_score
from scripts.polynomial_features import polynomial_features
from scripts.data_processing import *
from sklearn.preprocessing import StandardScaler
from scripts.linear_regression import CustomLinearRegression

def question_4():

    y_pred = np. array ([1 , 2, 3, 4, 5])
    y1 = np. array ([1 , 2, 3, 4, 5])

    print(r2_score(y_pred, y1))

    y2 = np. array ([3 , 5, 5, 2, 4])
    print(r2_score(y_pred, y2))

def question_8():
    X = np.array([[1 , 2],
                    [2, 3],
                    [3, 4]])
    print(polynomial_features(X))


def question_10():
    file_path = 'data/SalesPrediction.csv'
    test_size = 0.33
    df = load_data(file_path)
    df = process_data(df)
    X, y = get_features(df)
    X_train, _, _, _ = data_split(X, y, test_size=test_size)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    print(scaler.mean_[0])


def train_and_eval_custom_model(X_train, y_train, X_test, y_test):
    model = CustomLinearRegression(X_train, y_train)
    model.fit()
    pred_y = model.predict(X_test)
    print("y_test: ", y_test)
    print("pred_y: ", pred_y)
    score = r2_score(y_test, pred_y)
    print("Custom model score: ", score)

def train_and_eval_sklearn_model(X_train, y_train, X_test, y_test):
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_train, y_train)
    pred_y = model.predict(X_test)
    print("y_test: ", y_test)
    print("pred_y: ", pred_y)
    score = r2_score(y_test, pred_y)
    print("Sklearn model score: ", score)


if __name__ == "__main__":
    print("Question 4:")
    question_4()
    print("Question 8:")
    question_8()
    print("Question 10:")
    question_10()

    print("-"*100 + "")
    print("Sales prediction:")
    
    file_path = 'data/SalesPrediction.csv'
    test_size = 0.33
    X_train, X_test, y_train, y_test = prepare_data(file_path, test_size)
    print("-"*100)
    print("Training and evaluating custom model:")
    print("-"*100)

    train_and_eval_custom_model(X_train, y_train, X_test, y_test)
    
    print("\n" + "-"*100)
    print("Training and evaluating sklearn model:")
    print("-"*100)

    train_and_eval_sklearn_model(X_train, y_train, X_test, y_test)
