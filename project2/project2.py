﻿
from math import *
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => "))
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) #поставил двойные ковычки в конце
di=a*sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #убрал ненужную скобку
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print("Ristküliku pindala", S) #поменял двойные ковычки в конце 
P=2*(b+c)
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2+c**2)
print("Ristküliku diagonaal"), round(di,2)
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))
d=2*r
print("Ringi läbimõõt"+ str(d))
S=pi*r**2
print("Ringi pindala", round(S,2))
C=2*pi()*r
print("Ringjoone pikkus"), round(C,2) #закрыл скобку