 # -*- coding: utf-8 -*-
from math import *
# (1.) * (2) = (2.) - float * int = float
# (1.) * (2.)= (2.) - float * float = float
# Python 2.x
# x = 1. * input("Lietotāj, lūdzu, ievadi argumentu (x): ")
# Python 2.x
# x = float(raw_input("Lietotāj, lūdzu, ievadi argumentu (x): "))
# Python 3.x
x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = sin(x)
print("sin(%.2f) = %.2f"%(x,y))
a0 = (-1)**0*x**1/(1)
S0 = a0
print("a0 = %.2f S0 = %.2f"%(a0,S0))
a1 = (-1)**1*x**3/(1*2*3)
S1 = a0 + a1
print("a1 = %.2f S1 = %.2f"%(a1,S1))
a2 = (-1)**2*x**5/(1*2*3*4*5)
S2 = a0 + a1 + a2
print("a2 = %.2f S2 = %.2f"%(a2,S2))
a3 = (-1)**3*x**7/(1*2*3*4*5*6*7)
S3 = a0 + a1 + a2 + a3
print("a3 = %.2f S3 = %.2f"%(a3,S3))
a4 = (-1)**3*x**7/(1*2*3*4*5*6*7*8*9)
S4 = a0 + a1 + a2 + a3 + a4
print("a4 = %.2f S4 = %.2f"%(a4,S4))
a5 = (-1)**5*x**9/(1*2*3*4*5*6*7*8*9*10*11)
S5 = a0 + a1 + a2 + a3 + a4 + a5
print("a5 = %.2f S5 = %.2f"%(a5,S5))
a6 = (-1)**7*x**11/(1*2*3*4*5*6*7*8*9*10*11*12*13)
S6 = a0 + a1 + a2 + a3 + a4 + a5 + a6
print("a6 = %.2f S6 = %.2f"%(a6,S6))
a7 = (-1)**9*x**13/(1*2*3*4*5*6*7*8*9*10*11*12*13*14*15)
S7 = a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7
print("a7 = %.2f S7 = %.2f"%(a7,S7))
