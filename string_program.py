# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:54:29 2019

write a program to capture the string and the output in terms of list

enter any list: perl, unix, spark,scala
list output : ['perl', unix, spark,scala]
length of list : 4

@author: NSuryawanshi
"""


alist=(input("Enter values from keybard:"))
blist=alist.split(",")
print("List outout is :", alist)
print("List outout is :", blist)
print("Lenghth of list is :",len(blist))
