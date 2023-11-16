#Julio Alexis González Villa 220839961
#Natalie Xiomara Moreno Bautista  220839996

#----------------------------------Actividad 7_Detección de Colores------------------------------------

import serial
import numpy as np
import pickle 

serialPort = serial.Serial(port = "COM3", baudrate=9600)
serialString = ""

color = ['Rojo','Naranja','Amarillo','Verde','Limon','Azul','Marino','Cielo','Rosa','Morado','Cafe','Negro','Gris','Blanco']

model = pickle.load(open('act_7_colores.sav','rb'))

N = 100
i = 0

while(i<N):
    if(serialPort.in_waiting > 0):
        serialString = serialPort.readline()
        # print(serialString.decode('Ascii'))

        data_in = serialString.decode('Ascii')
        data_in = data_in.split(sep=',')
        data_in.pop()
        
        if(len(data_in)==4):
            data = [float(j) for j in data_in]
            data_array = np.asanyarray(data)
            
            y = model.predict(data_array.reshape(-1, 4))
            #i = i + 1
            d = y[0]
            print('iteration:',i,', data=',data_in, ', color=', color[d])
            i = i + 1
            
serialPort.close()
