import numpy as np
import matplotlib.pyplot as plt

def data_generator(N):
    X = np.random.uniform(0, 40 , N)
    Y = X * 2 + np.random.normal(0 , 2, N)
    X = X.reshape(-1,1)
    Y = Y.reshape(-1,1)
    print(X.shape)
    print(Y.shape)
    return X,Y

N = 200
X_train, Y_train = data_generator(N)

# یک پیچ تنظیم برای تنبیه و تغییر در نرخ آموزش . کارش کنترل تغییرات شیب خط است
lr = 0.0001

#  چون در شبکه های عصبی عملیات ترن  تدریجی است ابتدا یک ماتریس 1در1 میسازیم با یک عدد رندوم
w = np.random.rand(1, 1 )
print('First Random W is ---->' , w)

fig , ax = plt.subplots()

for i in range (N):
    #TRAIN
    # چون فقط یک مقدار را در خو نگه میدارد از حرف کوچیک استفاده کردیم
    y_pred = np.matmul(X_train[i], w)
    # محاسبه میزان تفاضل پیش بینی و واقعیت که ممکن است 
    e = Y_train[i] - y_pred
    # به منظور آپدیت شیب خط
    # باید "ایکس آموزش" رو هم بزاریم که بداند برای کدام داده ورودی این تغییر باید ایجاد شد
    w = w + e * lr * X_train[i]
    print('Updated W is ---->' , w)
    #PLOT
    # این را میسازیم دوباره اینجا که بتوانیم پلات کنیم
    Y_pred = np.matmul(X_train , w)
    ax.clear()
    plt.scatter(X_train,Y_train , c = 'red')
    ax.plot (X_train, Y_pred, c = 'green' , lw = 2)
    plt.pause(0.1)
