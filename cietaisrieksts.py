# -*- coding: utf-8 -*-
from math import *

def manssin(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a

    while True:
        k = k + 1
        R = (-1)*x*x/((2*k)*(2*k+1))
        a = a * R
        S = S + a
        if abs(sin(x)-S) < 0.01:
            k = k - 1
            return k

x = pi
y = manssin(x)
p = u"\u03C0"
print("Pie argumenta vertibas %s kluda starp teoretisko un praktisko ar summesanu ieguto tuvinajumu bus verojama pie locekla nr.%i"%(p,y))
