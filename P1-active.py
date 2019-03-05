#program to implement activation functions
import numpy as np
import random
import math

def identity(ynet):
    return ynet
    
def binary_step(ynet, threshold):
    if ynet>=threshold:
        return 1
    else:
        return 0
        
def sigmoid(ynet, lamda, mode):
    x = 1 + np.exp(-lamda*ynet)
    if mode=='binary':
        return 1/x
    if mode=='bipolar':
        z = 1 - np.exp(-lamda*ynet)
        return z/x

def ramp(ynet):
    if ynet>1:
        return 1
    if 0<=ynet<=1:
        return ynet
    if ynet<0:
        return 0
    
n_input = int(input('Enter no. of input nodes\t:'))
n_output = int(input('Enter no. of output nodes\t:'))
x = np.random.rand(1, n_input)
w = np.random.rand(n_input, n_output)
ynet  = np.matmul(x,w)
ynet = ynet.ravel()
print('\ninput = ',x)
print('weight = ',w)
print('ynet = ',ynet)

#Identity function
f = lambda x: identity(x)
output = f(ynet)
print('\nOutput by Identity function :',output)

#Binary step function
t = random.random()
output = [binary_step(x, t) for x in ynet]
print('\nOutput by Binary step function with theta='+str(t)+' :',output)

#Sigmoid function
l = random.random()
m = random.choice(['binary', 'bipolar'])
output = [sigmoid(x, l, m) for x in ynet]
print('\nOutput by Sigmoid function with lamda='+str(l)+' and mode='+str(m)+' :',output)

#Ramp function
output = [ramp(x) for x in ynet]
print('\nOutput by Ramp function :',output)
