import numpy as np
#Mean Difference of n_th Root Error
def md_nre_single_sample(y, y_hat, n, p):
    result = ((y**(1/n)) - (y_hat**(1/n)))**p
    return result


if __name__ == "__main__":
    print(md_nre_single_sample(y=10 , y_hat=8 , n=4 , p=3))  