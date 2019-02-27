# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:44:32 2019

@author: NSuryawanshi
"""

import os
# from current path
# print(os.listdir())  # To verify or list files 
v_list=os.listdir()

for val in v_list:
    if ".py" in val:
        print(val)
# from D:
#print(os.listdir("D:\\"))

# to remove os.unlink("filename")
# OR os.remove("filename")
        

v_list=os.listdir()

for val in v_list:
    if ".docx" in val:
        print("File is removed:", val)
        os.remove(val)  # to remove the file
        
# Program to convert .sh files to .ksh
        

        