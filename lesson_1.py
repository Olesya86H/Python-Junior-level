#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings

np.random.seed(0)

warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# Задание 0

# Реализуйте класс LinearRegressionSGD c обучением и и применением линейной регрессии, построенной с помощью стохастического градиентного спуска, с заданным интерфейсом.

# In[510]:


from sklearn.base import BaseEstimator

class LinearRegressionSGD(BaseEstimator):
    def __init__(self, epsilon=1e-4, max_steps=100, w0=None, alpha=1e-4):
        """
        epsilon: разница для нормы изменения весов 
        max_steps: максимальное количество шагов в градиентном спуске
        w0: np.array (d,) - начальные веса
        alpha: шаг обучения
        """
        self.epsilon = epsilon
        self.max_steps = max_steps
        self.w0 = w0
        self.alpha = alpha
        self.w = None
        self.w_history = []
    
    def fit(self, X, y):
        """
        X: np.array (l, d)
        y: np.array (l)
        ---
        output: self
        """
        l, d = X.shape
        
 
        if self.w0 is None:
          self.w0 = np.zeros(d)
 
        self.w = self.w0
 
        for step in range(self.max_steps):
        ## На каждом шаге градиентного спуска веса необходимо добавлять в w_history
          self.w_history.append(self.w)
         
          w_new = self.w - self.calc_gradient(X, y) + self.alpha #multiplying float on vector is not allowed - commented
 
          if (np.linalg.norm(w_new - self.w) < self.epsilon):
            break
          
          self.w = w_new       
        
        return self
    
    def predict(self, X):
        """
        X: np.array (l, d)
        ---
        output: np.array (l)
        """
        if self.w is None:
            raise Exception('Not trained yet')
        
        l, d = X.shape
 
        y_pred = []
 
        for i in range(l):
          y_pred.append(np.dot(X[i], self.w))
            
        return y_pred
    
    def calc_gradient(self, X, y):
        """
        X: np.array (l, d)
        y: np.array (l)
        ---
        output: np.array (d)
        """        
        l, d = X.shape
        gradient = []
        
        for j in range(d):            
            dQ = 0
            for i in range(l):  
                #dQ += (1/l) * (np.dot(X[j][i], self.w) - y[i])^2 * (np.dot(X[j][i], self.w) - y[i]) + self.w
                #dQ += (2/l) * X[i][j] * (np.dot(X[i], self.w) - len(y)) #y[i] - changed with len(y)\n",
                dQ += (2/l) * X[i][j] * (X[i] - len(y))
            gradient.append(dQ)

        return gradient


# Проверять работу мы будем на имеющемся в sklearn наборе данных boston: в нём нужно по информации о доме предсказать его стоимость.

# In[511]:


from sklearn.model_selection import train_test_split

data = pd.read_csv('boston.csv')
data = data.dropna()
num_features = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']
target = ['MEDV'] #это средняя цена домов, колонка, по которой мы будем прогнозировать результат
X = pd.DataFrame(data[num_features])
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(np.array(X), y, test_size=0.3, random_state=10)


# Задание 1

# Метрикой качества в нашей задаче будет MAPE - Mean Absolute Percentage Error. Реализуйте её с заданным интерфейсом и вычислите MAPE(y_test, y_0), где y_0 = (mean(y_test), mean(y_test), ...)

# In[512]:


def MAPE(y_true, y_pred):
    """
        y_true: np.array (l)
        y_pred: np.array (l)
        ---
        output: float [0, +inf)
    """
    y_test, pred = np.array(y_true), np.array(y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / y_true))
    return mape 


# In[513]:


y_0 = np.mean(y_test)
MAPE(y_test, y_0)


# Задание 2

# Обучите LinearRegressionSGD с базовыми параметрами на тренировочном наборе данных (X_train, y_train), сделайте предсказание на тестовых данных X_test, записав результат в переменную y_pred_sgd и вычислите ошибку MAPE.

# In[514]:


sgd = LinearRegressionSGD().fit(X_train, y_train)
y_pred_sgd = sgd.predict(X_test)
y_0 = np.mean(y_pred_sgd)
print("%.10f" %(MAPE(y_test, y_0)))


# Задание 3

# Вычислите веса по точной формуле, используя X_train и y_train; предскажите с их помощью целевую переменную на X_test, записав результат в переменную y_pred_lr и вычислите ошибку MAPE.

# In[515]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression().fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
y_0 = np.mean(y_pred_lr)
print("%.10f" %(MAPE(y_test, y_0)))


# Бонусное задание по неделе 4

# До этого вы релизовывали модели, в которых не было штрафа за величину весов w. Как было рассказано ранее в лекциях, это может привести к неустойчивости модели и переобучению. Чтобы избежать этих эффектов, предлагается добавить к оптимизируемому функционалу L2-норму весов; таким образом, будем решать задачу гребневой регрессии, Ridge:
# 
# 1l(Xw−y)T(Xw−y)+γ||w||2→minw.

# Задание 11

# Реализуйте обучение такой модели в матричном виде (смотрите дополнительные материалы к этой неделе) с помощью стохастического градиентного спуска. Класс должен совпадать по набору реализованных функций с LinearRegressionVectorized, разница будет лишь в параметре $\gamma$, отвечающем за степень регуляризации. 

# In[516]:


from sklearn.base import BaseEstimator

class RidgeSGD(BaseEstimator):
    def __init__(self, epsilon=1e-4, max_steps=100, w0=None, alpha=1e-4, gamma=1e-4):
        """
        epsilon: разница для нормы изменения весов 
        max_steps: максимальное количество шагов в градиентном спуске
        w0: np.array (d,) - начальные веса
        alpha: шаг обучения
        """
        self.epsilon = epsilon
        self.max_steps = max_steps
        self.w0 = w0
        self.alpha = alpha
        self.gamma = gamma
        self.w = None
        self.w_history = []
    
    def fit(self, X, y):
        """
        X: np.array (l, d)
        y: np.array (l)
        ---
        output: self
        """
        l, d = X.shape
        
 
        if self.w0 is None:
          self.w0 = np.zeros(d)
 
        self.w = self.w0
 
        for step in range(self.max_steps):
        ## На каждом шаге градиентного спуска веса необходимо добавлять в w_history
          self.w_history.append(self.w)
         
          w_new = self.w - self.calc_gradient(X, y) + self.gamma * self.alpha #multiplying float on vector is not allowed - commented
 
          if (np.linalg.norm(w_new - self.w) < self.epsilon):
            break
          
          self.w = w_new       
        
        return self
    
    def predict(self, X):
        """
        X: np.array (l, d)
        ---
        output: np.array (l)
        """
        if self.w is None:
            raise Exception('Not trained yet')
        
        l, d = X.shape
 
        y_pred = []
 
        for i in range(l):
          y_pred.append(np.dot(X[i], self.w))
            
        return y_pred
    
    def calc_gradient(self, X, y):
        """
        X: np.array (l, d)
        y: np.array (l)
        ---
        output: np.array (d)
        """        
        l, d = X.shape
        gradient = []
        
        for j in range(d):            
            dQ = 0
            for i in range(l):  
                #dQ += (1/l) * (np.dot(X[j][i], self.w) - y[i])^2 * (np.dot(X[j][i], self.w) - y[i]) + self.w
                #dQ += (1/l) * X[i][j] * (np.dot(X[i], self.w) - len(y)) #y[i] - changed with len(y)\n",
                dQ += (1/l) * X[i][j] * (X[i] - len(y))
            gradient.append(dQ)

        return gradient


# Так же, как и в основном задании, обучите модель с базовыми параметрами на тренировочных данных и сделайте прогноз y_pred_ridge. Выведите значение MAPE(y_test, y_pred_ridge).

# In[517]:


ridge = RidgeSGD().fit(X_train, y_train)
y_pred_ridge = ridge.predict(X_test)
y_0 = np.mean(y_pred_ridge)
print("%.10f" %(MAPE(y_test, y_0)))

