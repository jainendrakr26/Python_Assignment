# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 23:22:35 2020

@author: Jainendra
"""

for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
    
for i in range(5,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print("\r")