import math
import random
import numpy as np

def generate_sample(left = 0, right = 10):
    return random.uniform(left, right), random.uniform(left, right)

def loss_functions(num_samples, loss_name):
    if num_samples.isnumeric() == False:
        print("number of samples must be an integer number")
        return False
    
    num_samples = int(num_samples)

    # Mean Absolute Error
    def mae(samples):
        return np.sum(np.abs(samples[:,0] - samples[:,1])) / samples.shape[0]
    
    # Mean Squared Error
    def mse(samples):
        return np.sum((samples[:,0] - samples[:,1])**2) / samples.shape[0]
    
    # Root Mean Squared Error
    def rmse(samples):
        return np.sqrt(np.sum((samples[:,0] - samples[:,1])**2) / samples.shape[0])
    
    functions = {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse
    }

    samples = []
    losses = []
    for i in range(num_samples):
        sample = generate_sample()
        samples.append(sample)
        loss = (sample[0] - sample[1])**2
        if loss_name == 'MAE':
            loss = math.sqrt(loss)
        losses.append(loss)

    samples = np.array(samples)
    losses = np.array(losses)
    final_loss = functions[loss_name](samples)

    for i in range(num_samples):
        print(f'loss_name: {loss_name}, sample: {i}, pred: {samples[i][0]}, target: {samples[i][1]}, loss: {losses[i]}')
    print(f'final {loss_name}: {final_loss}')

    return True


if __name__ == "__main__":
    num_samples = input("Input number of samples ( integer number ) which are generated : ")
    loss_name = input("Input loss name : ")
    loss_functions(num_samples, loss_name)