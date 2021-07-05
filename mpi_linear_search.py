# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 11:44:34 2020

@author: fatih
"""

from mpi4py import MPI
import time
import numpy as np

def search(arr,aranan):
    for x in arr:
        if x==aranan:
            return 1
    return -1

comm=MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()

start_time = time.time()
aranan=9999999

if rank==0:
    arr=np.array([x for x in range(10000000)])
else:
    arr=None
    
arr2=np.empty([int(10000000/size)],dtype=int)
comm.Scatter(arr,arr2,root=0)

result=search(arr2, aranan)

if result==1:
    print("--bulundu-- İşlemci : ",rank)
    print("--- %s saniye ---\n" % (time.time() - start_time))
else:
    print("--bulunamadı-- İşlemci : ",rank)
    print("--- %s saniye ---\n" % (time.time() - start_time))