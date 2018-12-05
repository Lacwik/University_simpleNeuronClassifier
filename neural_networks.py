from activation_functions import *
import random


class Network1:
    def __init__(self):
        self.wages = []
        for i in range(0, 2):
            self.wages.append(random.uniform(0.1, 1.0))

    def compute(self, x, y, function='sigmoid'):
        sum = x*self.wages[0] + y*self.wages[1]
        if function == 'linear':
            return linear(sum)
        if function == 'unipolar':
            return unipolar(sum)
        if function == 'sigmoid':
            return sigmoid(sum)


class Network2:
    def __init__(self, const_signal):
        self.wages = []
        self.signal = const_signal
        for i in range(0, 2):
            self.wages.append(random.uniform(0.1, 1.0))

    def compute(self, x, y, function='sigmoid'):
        sum = x * self.wages[0] + y * self.wages[1] + self.signal
        if function == 'linear':
            return linear(sum)
        if function == 'unipolar':
            return unipolar(sum)
        if function == 'sigmoid':
            return sigmoid(sum)


class Network3:
    def __init__(self):
        self.wages_in = []
        self.wages_in_out = []
        for i in range(0, 2):
            self.wages_in.append(random.uniform(0.1, 1.0))
            self.wages_in_out.append(random.uniform(0.1, 1.0))

    def compute(self, x, y, function='sigmoid'):
        if function == 'linear':
            out0 = linear(self.wages_in[0]*x)
            out1 = linear(self.wages_in[1]*y)
            sum = out0*self.wages_in_out[0] + out1*self.wages_in_out[1]
            return linear(sum)
        if function == 'unipolar':
            out0 = unipolar(self.wages_in[0]*x)
            out1 = unipolar(self.wages_in[1]*y)
            sum = out0*self.wages_in_out[0] + out1*self.wages_in_out[1]
            return unipolar(sum)
        if function == 'sigmoid':
            out0 = sigmoid(self.wages_in[0]*x)
            out1 = sigmoid(self.wages_in[1]*y)
            sum = out0*self.wages_in_out[0] + out1*self.wages_in_out[1]
            return sigmoid(sum)


class Network4:
    def __init__(self, bias):
        self.wages_in = []
        self.wages_in_out = []
        self.bias = bias
        for i in range(0, 2):
            self.wages_in.append(random.uniform(0.1, 1.0))
            self.wages_in_out.append(random.uniform(0.1, 1.0))

    def compute(self, x, y, function='sigmoid'):
        if function == 'linear':
            out0 = linear(self.wages_in[0]*x + self.bias)
            out1 = linear(self.wages_in[1]*y + self.bias)
            sum = out0*self.wages_in_out[0] + out1*self.wages_in_out[1]
            return linear(sum)
        if function == 'unipolar':
            out0 = unipolar(self.wages_in[0]*x + self.bias)
            out1 = unipolar(self.wages_in[1]*y + self.bias)
            sum = out0*self.wages_in_out[0] + out1*self.wages_in_out[1]
            return unipolar(sum)
        if function == 'sigmoid':
            out0 = sigmoid(self.wages_in[0]*x + self.bias)
            out1 = sigmoid(self.wages_in[1]*y + self.bias)
            sum = out0*self.wages_in_out[0] + out1*self.wages_in_out[1]
            return sigmoid(sum)