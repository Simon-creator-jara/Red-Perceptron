# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 17:06:19 2021

@author: Admin
"""

import numpy as np 

matriz=np.array([[1. ,0. ,0., 0.], [1. ,1. ,0. , 1.], [1. ,0. ,1. , 1.], [1. ,1. ,1. , 1.]])
w01=np.array([[0.5],[0],[0],[0]])
w11=np.array([[1],[0],[0],[0]])
w21=np.array([[0],[0],[0],[0]])
dk=np.zeros((4, 1))
ek=np.zeros((4, 1))
ecm=np.zeros((4, 1))
yk=np.zeros((4, 1))
suma=np.zeros((4, 1))

edef=1
while edef !=0.0:
    for i in range(len(matriz)):
        if i>=1 and ek[i-1] !=0:
            w01[i,0]=w01[i-1,0]+1*ek[i-1]*matriz[i-1,0]
            w11[i,0]=w11[i-1,0]+1*ek[i-1]*matriz[i-1,1]
            w21[i,0]=w21[i-1,0]+1*ek[i-1]*matriz[i-1,2]
        else:
            if i>=1 and ek[i-1] ==0:
                w01[i,0]=w01[i-1,0]
                w11[i,0]=w11[i-1,0]
                w21[i,0]=w21[i-1,0]
        print(i)
        suma[i,0]=w01[i,0]*matriz[i,0]+w11[i,0]*matriz[i,1]+w21[i,0]*matriz[i,2]
        dk[i,0]=matriz[i,3]
        if suma[i,0] >=0:
            yk[i,0]=1
        else:
            yk[i,0]=0
        ek[i,0]=dk[i,0]-yk[i,0]
        ecm[i,0]=0.5*((dk[i,0]-yk[i,0])**2)
    iterx= np.concatenate((w01,w11,w21,np.array([matriz[:,0]]).T,np.array([matriz[:,1]]).T,np.array([matriz[:,2]]).T,yk,dk,ek,ecm),1)
    edef=ecm[0,0]+ecm[1,0]+ecm[2,0]+ecm[3,0]
    print(iterx)
    if edef !=0.0:
        w01=np.array([[w01[3,0]],[0],[0],[0]])
        w11=np.array([[w11[3,0]],[0],[0],[0]])
        w21=np.array([[w21[3,0]],[0],[0],[0]])