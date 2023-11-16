import pandas as pd

data_Rojo = pd.read_csv('df_color_Rojo.csv')
data_Naranja = pd.read_csv('df_color_Naranja.csv')
data_Amarillo = pd.read_csv('df_color_Amarillo.csv')
data_Verde = pd.read_csv('df_color_Verde.csv')
data_V_Claro = pd.read_csv('df_color_V_Claro.csv')
data_Azul = pd.read_csv('df_color_Azul.csv')
data_A_Marino = pd.read_csv('df_color_A_Marino.csv')
data_A_Claro = pd.read_csv('df_color_A_Claro.csv')
data_Rosa = pd.read_csv('df_color_Rosa.csv')
#data_Fiusha = pd.read_csv('df_color_Fiusha.csv')
data_Morado = pd.read_csv('df_color_Morado.csv')
data_Cafe = pd.read_csv('df_color_Cafe.csv')
data_Negro = pd.read_csv('df_color_Negro.csv')
data_Gris = pd.read_csv('df_color_Gris.csv')
data_Blanco = pd.read_csv('df_color_Blanco.csv')

data = pd.concat([data_Rojo,data_Naranja,data_Amarillo,data_Verde,data_V_Claro,data_Azul,data_A_Marino,data_A_Claro,data_Rosa,data_Morado,data_Cafe,data_Negro,data_Gris,data_Blanco],axis=0)

data.to_csv('df_color.csv',index=False)