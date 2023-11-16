import serial
import numpy as np
import pickle 

serialPort = serial.Serial(port = "COM3", baudrate=9600)
serialString = ""

model = pickle.load(open('act_4_resistencias.sav','rb'))

N = 100
i = 0

while(i<N):
    if(serialPort.in_waiting > 0):
        serialString = serialPort.readline()
        data_in = serialString.decode('Ascii')
        data_in = data_in.split(sep=',')
        data_in.pop()
        
        if(len(data_in)==5): # Utilizar el tamaño de los datos
            data = [float(j) for j in data_in]
            data_array = np.asanyarray(data)
            y = model.predict(data_array.reshape(-1,1))
            print(y)
            
            i = i + 1
            

serialPort.close()



