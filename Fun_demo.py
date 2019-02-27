# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:40:57 2019

@author: NSuryawanshi
"""

#function body
## default argument

def add(vf,vs,vt=0):
    vtotal=vf+vs+vt
    return vtotal

vgett=add(10,20)
print("sum of values :",vgett)

vgett=add(10,20,30)
print("sum of values :",vgett)

vgett=add(10,20,30)
print("sum of values :",vgett)

#fnction body
# default argument

def add(sec, first):
    vtotal=first+sec
    return vtotal

vgett=add(first=10,sec=20)
print("sum:",vgett)

# 

def display(*data):
    print(data)
    
display(12,33,54,55,66)

def display1(*data1):
    print(data)
    for item in data:
        print(item)