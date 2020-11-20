import numpy as np
import pandas as pd
#define X size 
X = np.zeros((26*23,3))  #26 days data, 23 unique user id steps
wea = pd.read_csv('../weather.csv')
wea=np.array(wea)
print (wea.shape)
#Accumulate only the weather data from the array
wea=wea[1:27,1:4]   #26 days data, column: high temp, low temp, humidity
wea = np.asfarray(wea, float)
print (wea.shape)
#replicate weather for all the steps data
for x in range(23):
    X[26*x:26*(x+1),:]=wea   
ones_x = np.ones((26*23,1))

#create the X_matrix with Ones in the first column followed by weather data in the next
X_ = np.concatenate((ones_x,X),axis=1)

#load the steps data
steps = pd.read_csv('../steps_count.csv')
steps=np.array(steps)
print (steps.shape)
#create a matrix of just steps data, removing the IDs
y=steps[2:28,2:25]
y=np.reshape(y,(y.shape[0]*y.shape[1],1))
y = np.asfarray(y, float)
#define learning rate
alpha = 0.0001
#define the total number of iterations 
iters = 1000
#define initial weights
theta = np.array([[1.0,1.0,1.0,1.0]])

#compute the mean squared error
def computecost(X,y,theta):
    inner = np.power((np.matmul(X,theta.T)-y),2)
    return np.sum(inner)/(2*len(X))

result = computecost(X_,y,theta)
print(result)

#compute the gradient and update the cost
def gradientDescent(X,y,theta,alpha,iters):
    for i  in range(iters):
        theta = theta - (alpha/len(X))*np.sum((X@theta.T-y)*X,axis=0)
        cost = computecost(X,y,theta)
    return (theta,cost)

g,cost=gradientDescent(X_,y,theta,alpha,iters)
print(g,cost)
