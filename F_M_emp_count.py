# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:41:44 2019

@author: NSuryawanshi
"""

fobj=open("D:\\PY_programs\\git_files\\datasets\\employees.csv")
v_fcount=0
v_mcount=0

for line in fobj:
    line=line.strip()
    ##print(line)
    if "Female" in line:
        v_fcount=v_fcount+1
    if "Male" in line:
        v_mcount=v_mcount+1

print("No of male employee:", v_mcount)
print("No of female emp:", v_fcount)

fobj.close()

fobj=open("D:\\PY_programs\\git_files\\datasets\\employees.csv")
v_count=0

for line in fobj:
    v_count=v_count+1
    if v_count==1:
        continue
    else:
        line=line.strip()
        print(line)
        line1=line.split(",")
        v_sal=int(line1[4])
        if v_sal > 10000:
            print(line)
    
fobj.close() 

v_fname=time.starttime("%d%d%y_%H%m%S.csv")
print(v_fname)


fr=open("D:\\PY_programs\\git_files\\datasets\\employees.csv","r")
fw=open("D:\\PY_programs\\git_files\\datasets\\employeesbackup.csv","w")

for line in fr:
    line=line.strip()
    line=line.replace(")
    

# context manager
    with open("D:\\PY_programs\\git_files\\datasets\\employees.csv") as fobj:
        for line in fobj:
            print(line)
            
# context manager
with open("D:\\PY_programs\\git_files\\datasets\\employees.csv") as fobj:
    data=fobj.readlines()        
        
for line in data[4:10]:
    print(line)

