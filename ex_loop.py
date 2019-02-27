# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:45:34 2019

@author: NSuryawanshi
"""
'''
print("------Even in reverse------------")
for val in range(400,302,-2):
    print(val)
'''  


fixed="192.168.0."
for val in range(1,11):
    ip=fixed+str(val)
    print(ip)
    

fixed="192.168."
for val in range(0,11):
    ip=fixed+str(val)
    print(ip)
    for val2 in range(0,11):
        ip2=ip+"."+str(val2)
        print(ip2)

###
#OR
###
        
list1=[]
list2=[]
fixed="192.168."
for val in range(0,11):
    list1.append(fixed+"0."+str(val))
    list2.append(fixed+"1."+str(val))
for ip in list1:
    print(ip)
for ip in list2:
    print(ip)
