# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:07:16 2019

write a program to create some empty list and perform the below operation

1. append 100 to the list
2. append 60 to the list
3. append 30 to the list
4. append 1000 to the list
5. extend the list with 90,3543,53,43,42,534,10,10,10,20
6.remove the element 3543
7. pop the element which is at index 5.
8. find the element at the index 6

@author: NSuryawanshi
"""

alist=[]
print("values before clear :", alist)
#alist=alist.clear
alist.append(100)
alist.append(60)
alist.append(30)
alist.append(1000)
alist.extend([90,3543,53,43,42,534,10,10,10,20])
print("values of list :",alist)
alist.remove(3543)
print("values of list :",alist)
print("alist before pop:",alist)
popitem=alist.pop(5)
print("removed element:", popitem)
#print("element at index 6 : ",alist.index(6))
print("after pop:", alist)
