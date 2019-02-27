# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:22:11 2019

conditional statements

write a program to verify the file extension
if file endswith .py display "python file"
if file endswith .txt displya "text file"
if file endswith .csv  display "csv file"
if file endswith .pl   display "perl file"
if file endswith .ksh  display "korn shell file"

Enter any fileenmae:  hello.py
Input file is python file

Enter any filename : hello.c
input file is C source file
@author: NSuryawanshi
"""

fname=input("Enter anyfile name:")
blist=fname.split(".")

print("File extention:",blist[1])

if blist[1].lower()=="py":
    print("this is python")
elif blist[1].lower()=="txt":
    print("this is text")
elif blist[1].lower()=="csv":
    print("this is csv")
elif blist[1].lower()=="pl":
    print("this is perl")
elif blist[1].lower()=="ksh":
    print("this is korn")
else:
    print("non of from the list")
    
    
'''
a=10
b=20

if a < b:
    print("Inside if")
    print("A is less than B")
else:
    print("inside else")
    print("B is less than A")
    '''
'''
name=input("input any string")

if name.isupper():
    print("this is upper")
    
elif name.islower():
    print("this is lower")
    
elif name.isdigit():
    print(string is digit)
else:
    print("non of above")
'''