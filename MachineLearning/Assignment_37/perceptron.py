from os import error
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class perceptron:
    def __init__ (self):
        pass

    def fit(self, X, Y):
        self.X = X
        self.Y = Y
        
        x_range = np.arange(X[:, 0].min(), X[:, 0].max(), 0.01)
        y_range = np.arange(X[:, 1].min(), X[:, 1].max(), 0.01)
        fig = plt.figure(figsize=(6,6))
        ax = fig.add_subplot(111,projection='3d')

        lr = 0.001
        self.w = np.random.rand(2, 1)
        self.b = np.random.rand(1, 1)
        self.Error = []
        for i in range(self.X.shape[0]):
            y_pred = np.matmul(self.X[i], self.w) + self.b
            e = self.Y[i] - y_pred
            self.w += self.X[i, :].T * lr * e
            self.b += lr * e

            Y_pred = np.matmul(self.X, self.w) + self.b
            error = np.mean(np.abs(self.Y - Y_pred))
            self.Error.append(error)

            #ax.clear()
            x, y = np.meshgrid(x_range, y_range)
            z = self.w[0] * x + self.w[1] * y
            ax.plot_surface(x, y, z, cmap="coolwarm" , alpha= 0.4 )
            ax.scatter(X[:,0], X[:,1], Y , c='black')
            ax.set_xlabel('X1')
            ax.set_ylabel('X2')
            ax.set_zlabel('Y')
            plt.pause(0.1)
            
            ax2 =plt.subplot(1, 2, 2)
            x = np.arange(0, len(self.Error))
            ax2.plot(x, self.Error)
            plt.pause(0.01)
            plt.xlabel('iteration')
            plt.ylabel('Cost')
        plt.show()
        return self.w, self.b

    def predict (self, X):
        Y=[]
        for i in range(X.shape[0]):
            y_pred=np.matmul(X[i], self.w) + self.b
            if y_pred>0:
                Y.append(1)
            else:
                Y.append(-1)
        return Y

    def acc(self,X,Y):
        y_predict = self.predict(X)
        cnt=0
        for i in range(len(Y)):
            if y_predict[i]==Y[i]:
                cnt+=1
        accuracy=cnt/len(Y)
        print('Accuracy --->' , accuracy)
        return accuracy

data1 = np.array(pd.read_csv('D:\linear_data_train.csv'))
X_train = np.matrix(data1[:, 0:2])
Y_train = np.array(data1[:, 2])

data2 = np.array(pd.read_csv('D:\linear_data_test.csv'))
X_test = np.matrix(data2[:, 0:2])
Y_test = np.array(data2[:, 2])

model = perceptron ()
model.fit(X_train,Y_train)
Predicton = model.predict(X_test)
model.acc(X_test, Y_test)
model.acc(X_train, Y_train)

