# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:14:41 2024

@author: ADMIN
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

ln=a
if ln<b:
    ln=b
elif ln<c:
    ln=c
print(f"giá trị lớn nhẩt là: {ln}")
