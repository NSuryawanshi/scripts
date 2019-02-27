# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:58:29 2019

Validate ip is valid or not

@author: NSuryawanshi
"""

vip=input("Enter ip address:")
vval=vip.count(".")
print("count of . is :", vval)
print(vip.split("."))
alist=vip.split(".")
print("What is my list now :", alist)
for val in (1,4):
    if alist[val] in range(0,225):
        print("Entered ip is valid")
    else:
        print("Entered ip is not valid")
    