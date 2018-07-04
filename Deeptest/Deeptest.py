import numpy as np
from matplotlib import pyplot


def sigmoid(x):
    return 1/(1+np.exp(-x))





x= np.array([1,0.5])
W= np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
b= np.array([0.1,0.2,0.3])

al= np.dot(x,W)+b

print(al)

z=sigmoid(al)

print(z)
