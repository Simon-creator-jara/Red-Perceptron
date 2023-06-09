clear all
Matrix=[[1 0 0 0];[1 1 0 1];[1 0 1 1];[1 1 1 1]];
A=size(Matrix);
w01=[0.5;zeros(A(1,1)-1,1)];%%Tiene los valores de la clase si se quiere se cambia por rand
w11=[1;zeros(A(1,1)-1,1)];
w21=[0;zeros(A(1,1)-1,1)];
dk=zeros(A(1,1),1);
ek=zeros(A(1,1),1);
ecm=zeros(A(1,1),1);
yk=zeros(A(1,1),1);
suma=zeros(A(1,1),1);
edef=1;
while edef ~= 0
    for i=1:size(Matrix,1)
             if i>=2 & ek(i-1) ~= 0
                 w01(i,1)=w01(i-1,1)+1*ek(i-1)*Matrix(i-1,1);
                 w11(i,1)=w11(i-1,1)+1*ek(i-1)*Matrix(i-1,2);
                 w21(i,1)=w21(i-1,1)+1*ek(i-1)*Matrix(i-1,3);
             else
                 if i>=2 & ek(i-1) == 0
                     w01(i,1)=w01(i-1,1);
                     w11(i,1)=w11(i-1,1);
                     w21(i,1)=w21(i-1,1);
                 end
             end
            suma(i,1)=w01(i,1)*Matrix(i,1)+w11(i,1)*Matrix(i,2)+w21(i,1)*Matrix(i,3);
            dk(i,1)=Matrix(i,4);
             if suma(i,1)>=0
                 yk(i,1)=1;
             else
                 yk(i,1)=0;
             end
             ek(i,1)=dk(i,1)-yk(i,1);
             ecm(i,1)=0.5*((dk(i,1)-yk(i,1))^2);


    end 
Iter=[w01,w11,w21,Matrix(:,1),Matrix(:,2),Matrix(:,3),yk,dk,ek,ecm]
edef=ecm(1,1)+ecm(2,1)+ecm(3,1)+ecm(4,1);
if edef ~= 0
    w01=[w01(4,1);zeros(3,1)];
    w11=[w11(4,1);zeros(3,1)];
    w21=[w21(4,1);zeros(3,1)];
end

end 

