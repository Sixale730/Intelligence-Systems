import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn import linear_model
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error, r2_score, explained_variance_score

df = pd.read_csv('Actividad 1 - Regresión Linear\pop.csv')
x = np.asanyarray(df[['year']])
y = np.asanyarray(df[['pop']])

model = linear_model.LinearRegression()
model.fit(x,y)

yp = model.predict(x)

print('Coefficients(',model.intercept_,',',model.coef_,')')

#Regresion metrics
r2 = r2_score(y,yp)
print('R^2 =',r2)

plt.figure()
plt.grid()
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x,y,'ro')
plt.plot(x,yp,'m-',lw=2)
plt.legend(['Data','Prediction'])

plt.show()

