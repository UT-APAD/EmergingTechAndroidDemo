import numpy as np
import pandas as pd
#define X size 
X = np.zeros((26*23,3))
wea = pd.read_csv('/home/madhumitha/Desktop/Fall2018/IOT_TA/weather.csv')
wea=np.array(wea)
print (wea.shape)
wea=wea[1:27,1:4]
wea = np.asfarray(wea, float)
print (wea.shape)
for x in range(23):
    X[26*x:26*(x+1),:]=wea   
ones_x = np.ones((26*23,1))
#print (ones_x.shape)
#X_ = np.reshape(X,(21*21,1))
#print (X_.shape)
X_ = np.concatenate((ones_x,X),axis=1)
#print (X_)
#print (X_.shape)
steps = pd.read_csv('/home/madhumitha/Desktop/Fall2018/IOT_TA/steps_count.csv')
steps=np.array(steps)
print (steps.shape)
y=steps[2:28,2:25]
y=np.reshape(y,(26*23,1))
y = np.asfarray(y, float)
#print (y.shape)
#y = np.random.random_sample((10,1))
alpha = 0.0001
iters = 1000
theta = np.array([[1.0,1.0,1.0,1.0]])

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
