# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:04:43 2019

write a program to remove all the duplicates from the list
alist=[10,20,10,20,30,40,50,20,30,40,60,70,80,10]
output:[10,20,30,40,50,60,70,80]

@author: NSuryawanshi
"""

alist=[10,20,10,20,30,40,50,20,30,40,60,70,80,10]
blist=set(alist)

print("OutPut after removing duplicate:",blist)

