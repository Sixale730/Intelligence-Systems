%% Regresión no Lineal - Kernel Ridge %%
% Sistemas Inteligentes IV%
% Julio Alexis González Villa%

clear 
close all
clc

%Leemos los datos del archivo
% T = readtable('df_regresion_nolineal_1.csv');
% T = readtable('df_regresion_nolineal_2.csv');
T = readtable('df_regresion_nolineal_3.csv');
% T = readtable('temp.csv');

%Variables de df_regresion_nolineal 1,2,3
x = T.x;
Y = T.y;

%Variables de temp
% x = T.time;
% Y = T.temp;

%Tipos de Kernel
%Lineal
% k = @(xi,xj) xi*xj'+1; 

%Polinómica
% k = @(xi,xj) (xi*xj'+1)^3;

%Base Radial
% k = @(xi,xj) exp(-0.1*norm(xi-xj)^2);

%Sigmoide
k = @(xi,xj) tanh(-0.1*(xi*xj')+1); 

n = size(x,1);
K = zeros(n,n);

for i=1:n
    for j=1:n
        K(i,j) = k(x(i,:),x(j,:));
    end
end

lambda = 0.001;
alpha = inv(K+lambda*eye(n,n))*Y;
Yp = K*alpha;


%Coeficiente R2
R2 = 1-(sum((Y-Yp).^2))/(sum((Y-mean(Y)).^2));

%Gráficas
figure 
title('Kernel Ridge Sigmoidal')
hold on 
grid on 
plot(x,Y,'bx','linewidth',2)
plot(x,Yp,'r-','linewidth',2)


