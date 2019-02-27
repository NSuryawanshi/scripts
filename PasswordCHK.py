# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:36:18 2019

Password verification program

@author: NSuryawanshi
"""

vpwd=input("Please enter strong password:")

if len(vpwd) > 6 and len(vpwd) < 12:
    alist=list(vpwd)
    print("Password after in lins:", alist)
    for val in range (0,len(vpwd)):
      if alist[val]=="@":
          print("Password is strong")
          break
      elif alist[val]=="#":
          print("Password is strong")
          break
      elif alist[val]=="&":
          print("Password is strong")
else:
    print("Password is not strong")


          
      
          
      