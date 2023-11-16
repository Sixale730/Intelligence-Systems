import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.pipeline import Pipeline
from sklearn.kernel_ridge import KernelRidge
import pickle


df = pd.read_csv('V_Resistencias.csv')
x = np.asanyarray(df[['Voltaje']])
y = np.asanyarray(df[['Resistencia']])
x_train, x_test, y_train, y_test = train_test_split(x,y)

model = Pipeline([('scaler',StandardScaler()),
                  ('reg',KernelRidge(alpha=0.0001, kernel='rbf'))])
model.fit(x,y)

pickle.dump(model,open('V_Resistencias.sav','wb'))

yp = model.predict(x)

plt.figure()
plt.grid()
plt.title('Regresion no lineal')
plt.xlabel('Voltaje')
plt.ylabel('Resistencia')

plt.plot(x,y,'mo')
plt.plot(x_test,y_test,'go')
plt.plot(x,yp,'-',lw=2)

plt.legend(['Muestras','Generalizacion', 'Predicción'])
plt.show()


e3 = r2_score(y,yp)
print('R^2 =',e3)
