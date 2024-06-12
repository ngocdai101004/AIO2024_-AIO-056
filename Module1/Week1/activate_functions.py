import math


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def activate_functions(x, function):
    if not is_number(x):
        print('x must be number')
        return False

    x = float(x)

    def sigmoid(x):
        return 1.0 / (1.0 + math.exp(-x))

    def relu(x):
        return max(0, x)

    def elu(x, alpha=0.01):
        return alpha * (math.exp(x) - 1) if x <= 0 else x

    functions = {
        "sigmoid": sigmoid,
        "relu": relu,
        "elu": elu
    }

    if function not in functions.keys():
        print(f'{function} is not supported')
        return False

    result = functions[function](x)
    print(f'{function}: f({x}) = {result}')


if __name__ == "__main__":
    x = input("Input x = ")
    function = input("Input activation Function ( sigmoid | relu | elu ) : ")
    activate_functions(x, function)
