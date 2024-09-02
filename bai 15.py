# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:46:29 2024

@author: HP
"""

import math
a=float(input("nhap a: "))
b=float(input("nhap b: "))
c=((a+b)/((a**(1/3)+(b**(1/3))))-((a*b)**(1/3)))/(a**(1/3)-b**(1/3))**2
print(c)
