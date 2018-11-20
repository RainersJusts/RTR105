# -*- coding: utf-8 -*-
from math import cos

def manscos(x):
    k = 0
    a = (-1)**0*x**0/(1)
    S = a
    print("a0 = %6.2f S0 = %6.2f"%(a,S))

    while k < 500:
        k = k + 1
        R = (-1)*x*x/((2*k)*(2*k-1))
        a = a * R
        S = S + a
        if k == 499:
            print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))

    print("a500 = %6.2f S500 = %6.2f"%(a,S))
    S = 1/2 + S/2
    return S
    
print("cos(x/2)*cos(x/2) aprekinasana:")
f = input("Ievadi argumentu (x): ")
x = float(f)
y = cos(x/2)*cos(x/2)
print("cos(%.2f) = %6.2f"%(x,y))

print("")

yy = manscos(x)
a = u"\u221E"
print("cos(%.2f)*cos(%.2f) caur summu = %6.2f"%(x,x,yy))
print("")
print("")
print("                             500")
print("                           -------")
print("                           \           k     2k")
print("                    1   1   \      (-1)  *  x")
print("cos(x/2)*cos(x/2) = - + -    |    ---------------    , kur - %s < x < %s"%(a,a))
print("                    2   2   /         (2*k)!")
print("                           /")
print("                           -------")
print("                            k = 0")
print("")
print("")
print("                                      2")
print("                                     x")
print("rekurences reizinatajs = (-1)* ---------------")
print("                                (2*n-1)*(2*n)")
