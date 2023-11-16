import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn import linear_model
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error, r2_score, explained_variance_score

df = pd.read_csv('Actividad 1 - Regresión Linear\salary.csv')
x = np.asanyarray(df[['YearsExperience']])
y = np.asanyarray(df[['Salary']])

model = linear_model.LinearRegression()
model.fit(x,y)

yp = model.predict(x)

#print(x)

p = model.predict([[15]])

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
plt.plot(x,p,'go',lw=2)
plt.legend(['Data','Prediction'])

plt.show()

