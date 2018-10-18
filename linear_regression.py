##linear regression with just numpy

import numpy as np
X = np.random.random_sample((10,1))
print(np.shape(X))
#X = np.transpose(X)
X = np.concatenate([np.ones((10,1)),X],1)
print(np.shape(X))
print(X)
y = np.random.random_sample((10,1))
alpha = 0.0001
iters = 100
theta = np.array([[1.0,1.0]])
def computecost(X,y,theta):
    inner = np.power(((X@theta.T)-y),2)
    return np.sum(inner)/(2*len(X))
result = computecost(X,y,theta)
print(result)
def gradientDescent(X,y,theta,alpha,iters):
    for i  in range(iters):
        theta = theta - (alpha/len(X))*np.sum((X@theta.T-y)*X,axis=0)
        cost = computecost(X,y,theta)
    return (theta,cost)
g,cost=gradientDescent(X,y,theta,alpha,iters)
print(g,cost)
