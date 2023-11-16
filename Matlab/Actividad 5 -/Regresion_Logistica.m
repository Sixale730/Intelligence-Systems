%% Regresión Logística %%
% Sistemas Inteligentes IV%
% Julio Alexis González Villa%

clear all
close all 
clc


%Leemos los archivos
%T = readtable('df_clasificacion_1.csv');
% T = readtable('df_clasificacion_2.csv');
T = readtable('df_clasificacion_3.csv');

x1 = T.x1;
x2= T.x2;
Y = T.y; 
D = 1;
X = Polynomial_Features(x1,x2,D);

[n,m] = size(X);
w = rand(m,1);
alpha = 0.2;
lambda = 0.001;

TPR_plot = [];
FPR_plot = [];

for i=1:n
    h = X*w;
    g = 1./(1+exp(-h));
    w = w*(1-alpha*lambda)+alpha*X'*(Y-g);
end 

figure
hold on
grid on 
plot(x1(Y==0), x2(Y==0), 'ro')
plot(x1(Y==1), x2(Y==1), 'bo')

Draw_Decision_Boundary (x1,x2,w,D)
drawnow

h = X*w;
g = 1./(1+exp(-h));

Yp = (g>=0.5)*1.0;

TN = 0; FP = 0; FN = 0; TP = 0;

for i=1:n
    if Y(i)==0 && Yp(i)==0
        TN = TN +1;
    elseif Y(i)==0 && Yp(i)==1
        FP = FP+1;
    elseif Y(i)==1 && Yp(i)==0
        FN = FN+1;
    elseif Y(i)==1 && Yp(i)==1
        TP = TP+1;
    end 

end

Acc = (TP+TN)/(TP+TN+FP+FN);

%% Ploteo Matriz de Confusión
figure
confusionchart(Y,Yp)
title('Matriz de confusión')

for umbral=0:0.01:1
    Yp = (g>=umbral)*1.0;

    TN = 0; FP = 0; FN = 0; TP = 0; 

    for i=1:n
        if Y(i)==0 && Yp(i)==0
            TN = TN + 1;
        elseif Y(i)==0 && Yp(i)==1
            FP = FP + 1;
        elseif Y(i)==1 && Yp(i)==0
            FN = FN + 1;
        elseif Y(i)==1 && Yp(i)==1
            TP = TP + 1;
        end 
    end 

    TPR = TP/(TP+FN);
    FPR = FP/(FP+TN);

    TPR_plot = [TPR_plot TPR];
    FPR_plot = [FPR_plot FPR];
end

%% Ploteo curvas ROC
figure 
hold on 
grid on 
plot(FPR_plot, TPR_plot,'LineWidth', 2)
title('Curva ROC')