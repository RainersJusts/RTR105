# -*- coding: utf -8 -*-
from math import cos, fabs
from time import sleep

def f(x):
    return cos(x/2)*cos(x/2)-0.5

a = 1.1
b = 3.2

funa = f(a)
funb = f(b)

if ( funa*funb > 0.0):
    print("Dotaja intervala [%s, %s] skanju nav"%(a, b))
    sleep(1); exit()
else:
    print("Dotajaam intervaalaa sakne(s) ir!")

deltax = 0.0001

k = 0

while ( fabs(b-a) > deltax ):
    k = k + 1
    x = (a+b)/2; funx = f(x)
    if (funa*funx < 0. ):
        b = x
    else:
        a = x

realfunc = cos(x/2)*cos(x/2)

print("Sakne ir: ", x)
print("Funkcijas vērtība šajā punktā: ", realfunc)
print("Nepieciešamo iterāciju skaits intervālu dalīšanai uz pusēm:", k)
