import pandas as pd
import numpy as np


def read_data(filepath='advertising.csv'):
    df = pd . read_csv(filepath)
    data = df . to_numpy()
    keys = list(df.keys())
    return keys, data


def max_sales(data, keys):
    sales = data[:, keys.index('Sales')]
    max_value = np.max(sales)
    max_index = np.argmax(sales)
    return max_value, max_index


def average_tv(data, keys):
    return np.average(data[:, keys.index('TV')])


def sales_equal_or_greater_than_n(data, keys, n):
    sales = data[:, keys.index('Sales')]
    cnt = np.sum(np.where(sales >= n, 1, 0))
    return cnt


def average_radio(data, keys, n):
    radios = data[:, keys.index('Radio')]
    sales = data[:, keys.index('Sales')]
    avg = np.average(radios[sales >= n])
    return avg


def ques19(data, keys):
    sale_id = keys.index('Sales')
    news_id = keys.index('Newspaper')
    news_avg = np.average(data[:, news_id])
    right_data = data[data[:, news_id] > news_avg]
    s = np.sum(right_data[:, sale_id])
    return s


def ques20(data, keys):
    sales = data[:, keys.index('Sales')]
    avg_sale = np.average(sales)
    scores = np.full(sales.shape, fill_value='Bad', dtype='<U8')
    for i in range(sales.shape[0]):
        if sales[i] > avg_sale:
            scores[i] = 'Good'
        elif sales[i] == avg_sale:
            scores[i] = 'Average'
    return scores


def ques21(data, keys):
    sales = data[:, keys.index('Sales')]
    avg_sale = np.average(sales)
    dif = np.absolute(sales-avg_sale)
    A = sales[np.argmin(dif)]
    scores = np.full(sales.shape, fill_value='Bad', dtype='<U8')
    for i in range(sales.shape[0]):
        if sales[i] > A:
            scores[i] = 'Good'
        elif sales[i] == A:
            scores[i] = 'Average'
    return scores


if __name__ == '__main__':
    filepath = 'advertising.csv'
    keys, data = read_data(filepath)

    # Question 15
    max_sales_value, max_sales_index = max_sales(data, keys)
    print('Ques 15: Max: ', max_sales_value, '- Index: ', max_sales_index)

    # Question 16
    avg_tv = average_tv(data, keys)
    print('Ques 16: ', avg_tv)

    # Question 17
    cnt = sales_equal_or_greater_than_n(data, keys, 20)
    print('Ques 17: ', cnt)

    # Question 18
    avg_radio = average_radio(data, keys, 15)
    print('Ques 18: ', avg_radio)

    # Question 19
    q19 = ques19(data, keys)
    print('Ques 19: ', q19)

    # Question 20
    q20 = ques20(data, keys)
    print('Ques 20: ', q20[7:10])

    # Question 21
    q21 = ques21(data, keys)
    print('Ques 21: ', q21[7:10])
