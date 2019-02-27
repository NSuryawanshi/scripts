# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:45:34 2019

write a program to capture any filename from kayboard (data.csv)
and display filename and extention seperatly

Enter any filename: data.csvcilenmae: dataextention:csv

@author: NSuryawanshi
"""

fname=input("Enter any file name:")
print("entered filename is :",fname)

alist=fname.split(".")


print("Filename :", alist[0])
print("File extention is:", alist[1])

fname2=alist[0]+".log"
print("New filename :", fname2)