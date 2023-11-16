import serial
import numpy as np
import pandas as pd

serialPort = serial.Serial(port = "COM3", baudrate=9600)
serialString = ""

color = ['Rojo','Naranja','Amarillo','Verde','V_Claro','Azul','A_Marino','A_Claro','Rosa','Morado','Cafe','Negro','Gris','Blanco']
d = 8

lista_r = []
lista_g = []
lista_b = []
lista_rgb = []
lista_d = []

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
            
            lista_r.append(data_array[0])
            lista_g.append(data_array[1])
            lista_b.append(data_array[2])
            lista_rgb.append(data_array[3])
            lista_d.append(d)
            
            i = i + 1
            print('iteration:',i,', data=',data_in, ', color=', color[d])


serialPort.close()

data = {'R':lista_r,'G':lista_g,'B':lista_b,'RGB':lista_rgb,'D':lista_d}

df = pd.DataFrame(data)
df.to_csv('df_color_' + color[d] + '.csv',index=False)