%% Regresión Lineal %%
% Sistemas Inteligentes IV%
% Julio Alexis González Villa%

%% Limpiamos el workspace
close all
clc
%% Leemos el archvivo separado por comas
M = readtable('pop.csv');
%% Extraemos los datos por columnas
X = M.year;
Y = M.pop;
%% Obtenemos el tamaño de los datos en X
S = size(X,1);
%% Matriz de 1,Datos
Xm = [ones(S,1) X];
%% Pesos
W = inv(Xm'*Xm)*Xm'*Y;
%% Aplicamos la regresión
Yp = Xm*W;
%% Predicción
P = [1 2023]*W;
%% Graficamos los datos, la regresión lineal y la predicción
hold on
grid on
plot(X,Y,'rp')
plot(2023,P,'gx')
plot(X,Yp,'b-','lineWidth',1)
xlabel('x')
ylabel('y')

%% Metrica de regresión
R2 = 1-(sum((Y-Yp).^2)/(sum((Y-mean(Y)).^2)));
disp(R2);