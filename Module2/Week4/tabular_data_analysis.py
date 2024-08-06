import pandas as pd
import numpy as np
import matplotlib . pyplot as plt
import seaborn as sns


def correlation(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))

    if denominator == 0:
        return 0

    return numerator / denominator


if __name__ == '__main__':
    data = pd.read_csv('advertising.csv')

    # Question 5
    x = data['Radio']
    y = data['Newspaper']
    result = correlation(x, y)
    print('Question 5: Correlation between TV and Sales = ', round(result, 2))

    # Question 6
    features = ['TV', 'Radio', 'Newspaper']
    print('Question 6:')
    for feature_1 in features:
        for feature_2 in features:
            correlation_value = correlation(data[feature_1], data[feature_2])
            print(f"{feature_1} and {feature_2}: {
                  round(correlation_value, 2)}")

    # Question 7
    print('Question 7:')
    x = data['Radio']
    y = data['Newspaper']
    result = np.corrcoef(x, y)
    print(result)

    # Quetion 8
    print('Question 8:')
    # correlation matrix
    data_corr_coef = data.corr()
    print('Correlation matrix: \n', data_corr_coef)

    # Question 9
    print('Question 9: ')
    plt.figure(figsize=(10, 8))
    sns.heatmap(data_corr_coef, annot=True, fmt=".2f", linewidth=.5)
    plt.show()
