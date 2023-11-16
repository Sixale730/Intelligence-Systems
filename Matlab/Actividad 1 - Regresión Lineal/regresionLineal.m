%% Regresión Lineal %%
% Sistemas Inteligentes IV%
% Julio Alexis González Villa%

%% Limpiamos el workspace
close all
clc
%% Leemos el archvivo separado por comas
M = readtable('df_regresion_lineal_1.csv');
%% Extraemos los datos por columnas
X = M.x;
Y = M.y;
%% Obtenemos el tamaño de los datos en X
S = size(X,1);
%% Matriz de 1,Datos
Xm = [ones(S,1) X];
%% Pesos
W = inv(Xm'*Xm)*Xm'*Y;
%% Aplicamos la regresión
Yp = Xm*W;
%% Graficamos los datos y la regresión lineal
hold on
grid on
plot(X,Y,'rp')
plot(X,Yp,'b-','lineWidth',1)
xlabel('x')
ylabel('y')

%% Metrica de regresión
R2 = 1-(sum((Y-Yp).^2)/(sum((Y-mean(Y)).^2)));
R2;