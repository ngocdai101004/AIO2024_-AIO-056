import numpy as np

# Question 1


def compute_mean(x):
    return np.mean(np.array(x))

# Question 2


def compute_median(x):
    size = len(x)
    x = np.sort(x)
    if size % 2 == 0:
        return (x[int(size/2 - 1)] + x[int(size/2)])*0.5
    return x[int((size + 1) / 2)]

# Question 3


def compute_std(x):
    mean = compute_mean(x)
    variance = np.sum((np.array(x) - mean)**2)
    variance /= len(x)
    return np.sqrt(variance)

# Question 4


def compute_correlation_cofficient(x, y):
    x = np.array(x)
    y = np.array(y)
    N = len(x)
    numerator = N * x.dot(y) - np.sum(x)*np.sum(y)
    denominator = np.sqrt(N*np.sum(x**2)-np.sum(x)**2) * \
        np.sqrt(N*np.sum(y**2)-np.sum(y)**2)
    if denominator == 0:
        return 0
    return np.round(numerator / denominator, 2)


if __name__ == '__main__':
    # Question 1
    x = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
    print("Question 1: Mean = ", compute_mean(x))

    # Question 2
    x = [1, 5, 4, 4, 9, 13]
    print("Question 2: Median = ", compute_median(x))

    # Question 3
    x = [171, 176, 155, 167, 169, 182]
    print("Question 3: std = ", np.round(compute_std(x), 2))

    # Question 4
    X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
    Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
    print("Question 4: Correlation =", compute_correlation_cofficient(X, Y))
