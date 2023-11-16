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
                  ('reg',KernelRidge(alpha=0.001, kernel='sigmoid'))])
model.fit(x_train,y_train)

pickle.dump(model,open('V_Resistencias.sav','wb'))

yp = model.predict(x)

plt.figure()
plt.grid()
plt.title('Regresion Polinomial')
plt.xlabel('Voltaje (v)')
plt.ylabel('Resistencia (ohms)')

plt.plot(x,y,'bo')
plt.plot(x_test,y_test,'ro')
plt.plot(x,yp,'g-',lw=2)

plt.legend(['muestras','generalizacion', 'prediccion'])
plt.show()


e3 = r2_score(y,yp)
print('R^2 =',e3)
