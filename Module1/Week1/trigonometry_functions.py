import math


def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def approx_sin(x, n):
    result = 0
    for i in range(n+1):
        result += math.pow(-1, i) * (x**(2*i+1)) / factorial(2*i + 1)
    return result


def approx_cos(x, n):
    result = 0
    for i in range(n+1):
        result += math.pow(-1, i) * (x**(2*i)) / factorial(2*i)
    return result


def approx_sinh(x, n):
    result = 0
    for i in range(n+1):
        result += (x**(2*i+1)) / factorial(2*i + 1)
    return result


def approx_cosh(x, n):
    result = 0
    for i in range(n+1):
        result += (x**(2*i)) / factorial(2*i)
    return result


if __name__ == "__main__":
    x = input('x (rad) = ')
    n = input('n = ')
    x = float(x)
    n = int(n)
    print(f'sin({x}) = ', approx_sin(x, n))
    print(f'cos({x}) = ', approx_cos(x, n))
    print(f'sinh({x}) = ', approx_sinh(x, n))
    print(f'cosh({x}) = ', approx_cosh(x, n))
