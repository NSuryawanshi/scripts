# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:29:22 2019

@author: NSuryawanshi
"""

### syntax 
## range(start, stop, step)

print("------One to Nine------------")
for val in range(1,10):
    print(val)
    
print("------Even------------")
for val in range(2,10,2):
    print(val)
    
print("-------Odd-----------")
for val in range(1,10,2):
    print(val)
 
print("------Reverse ------------")
for val in range(10,1,-1):
    print(val)
    
# for loop with string    
name="python"
for char in name:
    print(char)

# for loop with list
alist=[10,20,30,40]
for val in alist:
    print(val)

# fol loop with dict   
book={"chap1":10,"chap2":20}
for key in book:
    print(key)
    print("Value :", book[key])