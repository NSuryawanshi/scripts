# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:13:46 2019

@author: NSuryawanshi
"""

fobj=open("D:\\PY_programs\\git_files\\datasets\\employees.csv")

for line in fobj:
    line=line.strip()
    line2=line.split(",")
    if line2[1]=="Female":
        print(line)
    
fobj.close()

## OR
for line in fobj:
    line=line.strip()
    if "Female" in line:
        print(line)