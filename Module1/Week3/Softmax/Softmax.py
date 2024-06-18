import torch
import torch.nn as nn
import math
import numpy as np


class Softmax (nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition


if __name__ == "__main__":
    data = torch . Tensor([1, 1, 300000])
    softmax = Softmax()
    output = softmax(data)
    print(output)
