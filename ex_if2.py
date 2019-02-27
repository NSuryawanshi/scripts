# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:54:05 2019

@author: NSuryawanshi
"""

## syntax : range(start,stop,stop)

name=input("input any string : ")

if name==name.upper():
    print("string is in upper case:")
    cname=name.lower()
    print("new lower case value:", cname)
elif name==name.lower():
    print("string is in lower case:")
    cname=name.upper()
    print("new upper case value:", cname)
else:
    print("string is nither in upper nor in lower case")
    
    
print("Length of string is :", len(name))


if len(name)<10:
    print("string is too small:")
elif len(name)>30:
    print("string is too big")
else:
    print("sting carecter size is more that 10 and less than 30")
    
    

