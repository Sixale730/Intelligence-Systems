%% Regresión no Lineal - Ridge %%
% Sistemas Inteligentes IV%
% Julio Alexis González Villa%

clear 
close all 
clc

%Leectura de los datos del archivo
 T = readtable('temp.csv');

%Variables del archivo
x = T.time;
Y = T.temp;

d = 12;
X = x.^(0:d);

lambda = 0.001;
I = eye(d+1, d+1);

w = inv(X'*X+lambda*I)*X'*Y;

Yp = X*w;


%Coeficiente R2
R2 = 1-(sum((Y-Yp).^2))/(sum((Y-mean(Y)).^2));


%Gráficas
figure 
title('Ridge')
hold on 
grid on 
plot(x,Y,'bx','linewidth',2)
plot(x,Yp,'r-','linewidth',2)