import math


def linear(x):
    result = 2*x
    return result


def unipolar(x):
    if x < 0:
        return 0
    else:
        return 1


def sigmoid(x):
    result = 1.0/(1.0+math.exp(-x))
    return result
