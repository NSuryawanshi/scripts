# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:45:26 2019

@author: NSuryawanshi
"""

## string methods
# everything is python object
# every object contains set of methods 

name = "pYthon"

print(name.upper())
print(name.capitalize())
print(name.lower())
print(name.upper())
print(name)


name1="unix,scala,spark,hadoop"

print(name1.split(","))

name2="   linux   "
print(name2.strip())


name3="linux programming"
print(name3.replace("linux","python"))

alist=[10,20,30,40]

print(alist.sort())

atup=(30,40,50)
print(atup.count())

adict={"chap1":10,"chap2":20,"chap3":30}
print(adict.keys("chap1"))



