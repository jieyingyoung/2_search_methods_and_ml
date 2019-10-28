from sklearn.datasets import load_boston
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def price_function(k,x,b):
    return k * x + b

def loss_function(y_real, y_pred):
    return sum((y_real_i-y_pred_i)**2 for y_real_i, y_pred_i in zip(list(y_real),list(y_pred))) / len(y_real)

def loss_with_respect_to_k(x, y_real, y_pred):
    return sum((y_real_i-y_pred_i)* x_i for y_real_i,y_pred_i,x_i in zip(list(y_real),list(y_pred),list(x))) / len(y_real) * (-2)

def loss_with_respect_to_b(y_real, y_pred):
    return sum((y_real_i-y_pred_i) for y_real_i,y_pred_i in zip(list(y_real),list(y_pred))) / len(y_real) * (-2)


dataset = load_boston()
dataX,dataY = dataset['data'],dataset['target']
# print(dataX.shape, dataY.shape)
dataPDX = pd.DataFrame(dataX)
print(dataPDX)
print(dataset.feature_names)

# take dataX[:,5} for example, the number of rooms
data_RM = dataX[:,5]
print(data_RM)
plt.scatter(data_RM,dataY)
plt.show()

# to initialize the parameters
k = random.random() * 200 - 100 # [-100 100) # random()返回随机生成的一个实数，它在[0,1)范围内
b = random.random() * 200 - 100

learning_rate = 1e-4
iteration_number = 1000
losses = []

for iteration in range(iteration_number):
    price_pred = [price_function(k,x_i,b) for x_i in data_RM]
    loss = loss_function(dataY, price_pred)
    losses.append(loss) # for later use, to plot the losses with respect to the iterations
    print('iteration:{},loss:{},k:{},b:{}'.format(iteration,loss,k,b))

    k_prime = loss_with_respect_to_k(data_RM, dataY, price_pred)
    b_prime = loss_with_respect_to_b(dataY, price_pred)
    k = k + (-1 * k_prime )  * learning_rate
    b = b + (-1 * b_prime ) * learning_rate

k_best = k
b_best = b

plt.plot(range(iteration_number),losses) # plot the losses as a function of iteration_number
plt.show()

price_pred_best = price_function(k_best,data_RM, b_best)
plt.scatter(data_RM,price_pred_best)
plt.scatter(data_RM,dataY)
plt.show()