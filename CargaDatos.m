%%Carga datos red perceptrón 


%%Limpiamos espacio de trabajo
clear;close all;clc

%%Cargamos base de datos
fprintf('Cargando base de datos');
load('BASE_DATOS.mat');%%Datos/nombre_base




%%Agregar el BIAS
entradas=[ones(1,size(entradas,2));entradas] ;
%%Normalizacion de los datos 
maxdeseados=(max(max(deseados)));
entradas=entradas./(max(max(entradas)));
deseados=deseados./(max(max(deseados)));
%%Analizamos la base de datos 
nd=size(entradas,2);
ne=size(entradas,1);
ns=size(deseados,1);

%%Mostramos la info al usuario
fprintf('Los datos tienen: \n');
fprintf('\t- Número de entradas= %d\n',ne);
fprintf('\t- Número de salidas= %d\n',ns);
fprintf('\t- Número de datos= %d\n',nd);

%%Preguntamos datos al usuario
alfa=input('Ingrese alfa: \n');
fprintf('OK.....');

%%Pidamos cantidad de iteraciones 
nit=input('Ingrese número de iteraciones: \n');
fprintf('OK....');

%%Creamos jmatriz de pesos neuronales
W=2.*rand(ns,ne)-1;


%%Creamos el vector de salidas.
Yk=zeros(ns,nd);

%%Creamos matriz de error cuadrático medio

ecm=zeros(ns,nit);


%%Entrenamos la red neuronal 
fprintf('Entrenando...\n');

for i=1:nit
    [Yk,ecm(:,i),W]= feedForwardPerceptron(alfa,entradas,deseados,W,1);
    fprintf('ECM iteracion %d: ',i);
    disp(ecm(:,i));
    fprintf('\n');
    
end

for j=1:ns
    plot(ecm(j,:));
    hold on 

end
% figure
% title(['Error salida',num2str(1)])
% plot(ecm(1,:));
% figure
% title(['Error salida',num2str(2)])
% plot(ecm(2,:));
% figure
% title(['Error salida',num2str(3)])
% plot(ecm(3,:));
Yk=Yk.*maxdeseados;

fprintf('W entrenado es: \n');
disp(W);
figure
plotconfusion(deseados,Yk,'Matriz de confusion');