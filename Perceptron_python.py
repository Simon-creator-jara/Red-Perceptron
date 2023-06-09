# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:39:24 2021

@author: Admin
"""
import numpy as np 

A=np.array([[1. ,0. ,0., 0.], [1. ,1. ,0. , 1.], [1. ,0. ,1. , 1.], [1. ,1. ,1. , 1.]])
class Perceptron:
    
    def __init__(self,matriz):
        import numpy as np
        self.matriz=matriz
        self.w01=np.array([[0.5],[0],[0],[0]])
        self.w11=np.array([[1],[0],[0],[0]])
        self.w21=np.array([[0],[0],[0],[0]])
        self.dk=np.zeros((4, 1))
        self.ek=np.zeros((4, 1))
        self.ecm=np.zeros((4, 1))
        self.yk=np.zeros((4, 1))
        self.suma=np.zeros((4, 1))
        self.edef=1
        
    def ciclo(self):

        while self.edef !=0:
            for i in range(len(self.matriz)):
                if i>=1 and self.ek[i-1] !=0:
                    self.w01[i,0]=self.w01[i-1,0]+1*self.ek[i-1]*self.matriz[i-1,0]
                    self.w11[i,0]=self.w11[i-1,0]+1*self.ek[i-1]*self.matriz[i-1,1]
                    self.w21[i,0]=self.w21[i-1,0]+1*self.ek[i-1]*self.matriz[i-1,2]
                else:
                    if i>=1 and self.ek[i-1] ==0:
                        self.w01[i,0]=self.w01[i-1,0]
                        self.w11[i,0]=self.w11[i-1,0]
                        self.w21[i,0]=self.w21[i-1,0]
                
                self.suma[i,0]=self.w01[i,0]*self.matriz[i,0]+self.w11[i,0]*self.matriz[i,1]+self.w21[i,0]*self.matriz[i,2]
                self.dk[i,0]=self.matriz[i,3]
                if self.suma[i,0] >=0:
                    self.yk[i,0]=1
                else:
                    self.yk[i,0]=0
                self.ek[i,0]=self.dk[i,0]-self.yk[i,0]
                self.ecm[i,0]=0.5*((self.dk[i,0]-self.yk[i,0])**2)
            print( np.concatenate((self.w01,self.w11,self.w21,np.array([self.matriz[:,0]]).T,np.array([self.matriz[:,1]]).T,np.array([self.matriz[:,2]]).T,self.yk,self.dk,self.ek,self.ecm),1))
            self.edef=self.ecm[0,0]+self.ecm[1,0]+self.ecm[2,0]+self.ecm[3,0]
            print("El error es: ",self.edef)
            if self.edef !=0:
                self.w01=np.array([[self.w01[3,0]],[0],[0],[0]])
                self.w11=np.array([[self.w11[3,0]],[0],[0],[0]])
                self.w21=np.array([[self.w21[3,0]],[0],[0],[0]])

   
x=Perceptron(A)
x.ciclo()
