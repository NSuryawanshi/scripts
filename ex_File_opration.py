# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:30:59 2019

@author: NSuryawanshi
"""

fobj=open("D:\\PY_programs\\New_domo.txt","w")
## OR
## fobj=open("D:/PY_programs/New_domo.txt","w")

for val in range(1,10):
    fobj.write(input("Write content of file:")+"\n")

fobj.close()


# Read line by line
fobj=open("D:\\PY_programs\\New_domo_read.txt","r")
for line in fobj:
    #remove whitesapce ant the end of file
    line=line.strip()
    print(line)
    # Split the line with , as delimeter 
    data=line.split(",")
    #display 1st field
    print(data[0])
fobj.close()


# Read line by line and prinf first field
fobj=open("D:\\PY_programs\\New_domo_read.txt","r")
for line in fobj:
    #remove whitesapce ant the end of file
    line=line.strip()
    #print(line)
    # Split the line with , as delimeter 
    data=line.split(",")
    #display 1st field
    print(data[0])
fobj.close()


