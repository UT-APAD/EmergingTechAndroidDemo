import numpy as np
import pandas as pd
#X = np.random.random_sample((10,1))
#print(np.shape(X))
#X = np.transpose(X)
X = np.zeros((21,21))
for x in range(21):
    X[:,x]=x   
ones_x = np.ones((21*21,1))
#print (ones_x.shape)
X_ = np.reshape(X,(21*21,1))
#print (X_.shape)
X_ = np.concatenate((ones_x,X_),axis=1)
#print (X_)
#print (X_.shape)
steps = pd.read_csv('/home/madhumitha/Desktop/Fall2018/IOT_TA/steps_count.csv')
steps=np.array(steps)
y=steps[1:22,1:22]
y=np.reshape(y,(21*21,1))
y = np.asfarray(y, float)
#print (y.shape)
#y = np.random.random_sample((10,1))
alpha = 0.0001
iters = 1000
theta = np.array([[1.0,1.0]])

def computecost(X,y,theta):
    inner = np.power((np.matmul(X,theta.T)-y),2)
    return np.sum(inner)/(2*len(X))

result = computecost(X_,y,theta)
print(result)

def gradientDescent(X,y,theta,alpha,iters):
    for i  in range(iters):
        theta = theta - (alpha/len(X))*np.sum((X@theta.T-y)*X,axis=0)
        cost = computecost(X,y,theta)
    return (theta,cost)
g,cost=gradientDescent(X_,y,theta,alpha,iters)
print(g,cost)
