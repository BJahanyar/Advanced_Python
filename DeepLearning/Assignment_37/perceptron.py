import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.array(pd.read_csv('D:\linear_data_train.csv'))

X_train = np.array(data[:, 0:2])
Y_train = np.array(data[:, 2])

N = X_train.shape[0]

lr = 0.001
w = np.random.rand(2, 1)

x_range = np.arange(X_train[:, 0].min(), X_train[:, 0].max(), 0.01)
y_range = np.arange(X_train[:, 1].min(), X_train[:, 1].max(), 0.01)

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111,projection='3d')

for i in range (N):
    print("Shape of X_train is ---->" , X_train.shape)
    #TRAIN
    y_pred = np.matmul(X_train[i] , w)
    e = Y_train[i] - y_pred
    w = w + lr * X_train[i, :].T * e

    ax.clear()
    x, y = np.meshgrid(x_range, y_range)
    z = w[0] * x + w[1] * y

    ax.plot_surface(x, y, z, rstride=1, cstride=1, alpha=0.4)
    ax.scatter(X_train[:,0], X_train[:,1], Y_train , c='black')
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Y')
    plt.pause(0.01)
plt.show()
