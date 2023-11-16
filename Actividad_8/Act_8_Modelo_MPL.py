#Julio Alexis Gonzalez Villa       220839961
#Natalie Xiomara Moreno Bautista   220839996
#Miguel Alejaandro Medina Bravo

#---------------------------Actividad 8_ Modelo------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.inspection import DecisionBoundaryDisplay
import pickle

from sklearn.neural_network import MLPClassifier


#
data = pd.read_csv('mnist_784.csv')
#print(data)

x = np.asanyarray(data.drop(columns=['class']))
y = np.asanyarray(data[['class']])

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)

#
model = Pipeline([('scaler',StandardScaler()),('cla',MLPClassifier(hidden_layer_sizes=(250,250,10),solver='adam',
                    activation='tanh',batch_size=5,max_iter=500,alpha=0.001))])

model.fit(x_train, y_train)

print('Train score',model.score(x_train,y_train))
print('Test score',model.score(x_test,y_test))


#
yp = model.predict(x)

disp = DecisionBoundaryDisplay.from_estimator(model,x,response_method="predict",alpha=0.5,eps=0.2,cmap=plt.cm.RdBu,xlabel='x1',ylabel='x2')
disp.ax_.scatter(x[y==0,0],x[y==0,1],color='r',edgecolor='k')
disp.ax_.scatter(x[y==1,0],x[y==1,1],color='b',edgecolor='k')

# Métricas
print('Metricas: \n', metrics.classification_report(y,yp))

# Matriz de Confusión
print('Confusion matrix: \n', metrics.confusion_matrix(y,yp))
