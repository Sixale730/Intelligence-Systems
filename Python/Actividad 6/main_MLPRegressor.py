import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.neural_network import MLPRegressor


#
df = pd.read_csv('temp.csv') # 1, 2, 3

x = np.asanyarray(df[['time']])
y = np.asanyarray(df[['temp']])

x_train, x_test, y_train, y_test = train_test_split(x, y)


#
model = Pipeline([('scaler',StandardScaler()),
                  ('reg',MLPRegressor(hidden_layer_sizes=(100,100,10),solver='adam',
                                      activation='tanh',batch_size=5,max_iter=500,alpha=0.001))])

model.fit(x_train,y_train.ravel())

print('Train score: ',model.score(x_train,y_train))
print('Test score: ',model.score(x_test,y_test))


#
x_plot = np.linspace(x.min(),x.max(),50).reshape(-1,1)
y_plot = model.predict(x_plot)

plt.figure()
plt.grid()
plt.title('Regresion no lineal')
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x_train,y_train,'bo')
plt.plot(x_test,y_test,'ro')
plt.plot(x_plot,y_plot,'k-',lw=2)

plt.legend(['entrenamiento','generalizacion','prediccion'])
plt.show()
