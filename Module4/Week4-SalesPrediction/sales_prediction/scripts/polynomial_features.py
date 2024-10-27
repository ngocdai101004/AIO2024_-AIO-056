import numpy as np



def polynomial_features(X, degree=2):

    X_mem = []
    for X_sub in X.T:
        X_new = X_sub
        for d in range(2, degree + 1):
            X_new = np.c_[X_new, X_sub ** d]
        X_mem.extend(X_new.T)
    X = np.c_[X_mem].T
    return X

