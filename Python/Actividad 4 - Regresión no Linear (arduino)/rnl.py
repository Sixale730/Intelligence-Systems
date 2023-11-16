import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import serial

df = pd.read_csv('Actividad 4 - Regresión no Linear (arduino)\V_Resistencias.csv')
x = np.asanyarray(df[['Resistencia']])
y = np.asanyarray(df[['Voltaje']])

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

#x_train, x_test, y_train, y_test = train_test_split(x,y)


from sklearn.kernel_ridge import KernelRidge

model = Pipeline([('scaler', StandardScaler()),
                  ('reg',KernelRidge(alpha=0.015, kernel='rbf'))])

model.fit(x,y)

print('Train Score: ', model.score(x,y))
#print('Test Score: ', model.score(x_test,y_test))

x_plot = np.linspace(x.min(),x.max(),50).reshape(-1,1)
y_plot = model.predict(x_plot)

plt.figure()
plt.grid()
plt.title('Regre')
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x,y,'mo')
#plt.plot(x_test,y_test,'ro')
plt.plot(x_plot,y_plot,'k-',lw=2)



plt.legend(['Train','Generalization','Prediction'])
plt.show()