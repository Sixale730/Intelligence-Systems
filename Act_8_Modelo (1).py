#Julio Alexis Gonzalez Villa 220839961
#Natalie Xiomara Moreno Bautista 220839996
#Miguel Alejandro Medina Bravo

#--------------------------------------Actividad 8_Modelo-----------------------------------------
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
#from sklearn.decomposition import PCA
from sklearn import metrics
import pickle

from sklearn.neighbors import KNeighborsClassifier


#
data = pd.read_csv('mnist_784.csv')
#print(data)

x = np.asanyarray(data.drop(columns=['class']))
y = np.asanyarray(data[['class']])

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)


# KNN
model = Pipeline([('scaler',StandardScaler()),('cla',KNeighborsClassifier(n_neighbors=12))])


model.fit(x_train,y_train.ravel())

print('Train score: ',model.score(x_train, y_train)) 
print('Test score: ',model.score(x_test, y_test))

pickle.dump(model,open('act_8_numeros.sav','wb'))

yp = model.predict(x)

print('Metricas: \n', metrics.classification_report(y,yp))
print('Confusion matrix: \n', metrics.confusion_matrix(y,yp))
