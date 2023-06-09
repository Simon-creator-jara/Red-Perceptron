function [Yk,ecm,W] = feedForwardPerceptron(alfa,entradas,deseados,W,entrena)
nd=size(deseados,2);
ns=size(deseados,1);

%%Creamos salida y ecm
Yk=zeros(ns,nd);
ecm=zeros(ns,1);

for i =1:nd
    %%Calculamos la agregación AJ
    Aj=W*entradas(:,i);
    
    %%Calculamos fn de activación
    Yk(:,i)= (Aj>=0);
    
    %%Calculamos el error 
    Ek=deseados(:,i)-Yk(:,i);
    
    %%Calculamos el ECM
    ecm(:)=ecm(:)+(Ek.^2)./2;
    
    
    %%Entrenamos 
    if entrena==1
        W=W+alfa*Ek*entradas(:,i)';
    end
    
end


end

