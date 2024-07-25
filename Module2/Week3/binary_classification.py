
import numpy as np


# ###################
# Create data
# ###################
def create_train_data():
    data = [['Sunny', 'Hot', 'High', 'Weak', 'no'],
            ['Sunny', 'Hot', 'High', 'Strong', 'no'],
            ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
            ['Rain', 'Mild', 'High', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
            ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
            ['Overcast', 'Mild', 'High', 'Weak', 'no'],
            ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    return np.array(data)


# ######################
# Prior Probability P(Y)
# ######################
def compute_prior_probablity(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np .zeros(len(y_unique))
    num = train_data.shape[0]

    for i, y in enumerate(y_unique):
        counter = sum(1 for row in train_data if row[-1] == y)
        prior_probability[i] = counter/num
    return prior_probability


# ###################
# Likelihood P(X|y)
# ###################
def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []
    for i in range(0, train_data . shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        list_x_prob = []
        for _, y in enumerate(y_unique):
            y_counter = sum(1 for row in train_data if row[-1] == y)
            prob_x = []
            for _, x in enumerate(x_unique):
                x_counter = sum(
                    1 for row in train_data if row[i] == x and row[-1] == y)
                prob_x.append(x_counter/y_counter)
            list_x_prob.append(prob_x)
        conditional_probability.append(list_x_prob)
    return conditional_probability, list_x_name


def get_index_from_value(feature_name, list_features):
    try:
        return np.nonzero(list_features == feature_name)[0][0]
    except NameError:
        return -1


# #########################
# Train Naive Bayes Model
# #########################
def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity(train_data)
    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)

    return prior_probability, conditional_probability, list_x_name


# ###################
# Prediction
# ###################
def prediction_play_tennis(x_condition, list_x_name, prior_probability, conditional_probability):

    x = []
    for i in range(4):
        x.append(get_index_from_value(x_condition[i], list_x_name[i]))

    p = []
    for i in range(2):
        prob = 1
        for j in range(4):
            prob *= conditional_probability[j][i][x[j]]
        prob *= prior_probability[i]
        p.append(prob)

    if p[0] > p[1]:
        y_pred = 0
    else:
        y_pred = 1
    print(p)
    return y_pred


if __name__ == '__main__':
    train_data = create_train_data()
    print(train_data)
    prior_probablity = compute_prior_probablity(train_data)
    print("P(play tennis = No) = ", prior_probablity[0])
    print("P(play tennis = Yes) = ", prior_probablity[1])
    train_data = create_train_data()
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)
    print(conditional_probability)
    print(list_x_name)
    X = ['Sunny', 'Cool', 'High', 'Strong']
    prior_probability, conditional_probability, list_x_name = train_naive_bayes(
        train_data)
    pred = prediction_play_tennis(
        X, list_x_name, prior_probablity, conditional_probability)
    if (pred):
        print('Ad should go!')
    else:
        print('Ad should not go!')
