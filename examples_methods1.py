# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:12:41 2019

@author: NSuryawanshi
"""

alist=[]
alist.append(30)
alist.append(40)

print("after appending :",alist)

#alist.clear()
#print(alist)

alist.extend([50,30,10,10,20])
print("after extending:",alist)

print("count of 10s :", alist.coun(10))

getindex=alist.index(30)

print("index of 20:",getindex)

#revers happends in place 

alist.reverse()
print(alist)

alist.sort()
print(alist)

print("alist before pop:",alist)
popitem=alist.pop(5)
print("removed element:", popitem)
print("after pop:", alist)


adict={"chap1":10,"chap2":20,"chap3":30, "chap4":100}
print("dict elements:",adict)
print("Only keys:", adict.keys())
print("onaly kets:", list(adict.keys()))
print("Only values :",adict.values())
print("only values in form of list :", tuple(adict.values()))
print("items:", adict.items())



