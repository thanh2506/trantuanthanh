# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:16:13 2024

@author: ADMIN
"""

gio = input("Nhập vào giờ, phút và giây theo định dạng hh:mm:ss: ")
hh, mm, ss = map(int, gio.split(':'))
a = hh * 3600 + mm * 60 + ss
print("Tổng số giây:", a ) 
